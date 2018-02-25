from datetime import datetime

from croniter import croniter
from django.db import models
from typing import List

from school_1329_server.common.tasks import send_notifications
from school_1329_server.groups.models import Group
from school_1329_server.users.models import User


class Notification(models.Model):
    text = models.CharField(max_length=200)

    created_by = models.ForeignKey(User, models.CASCADE)
    groups = models.ManyToManyField(Group)

    sent = models.BooleanField(default=False)
    send_once = models.BooleanField(default=True)

    # crontab mask: https://crontab.guru/
    frequency = models.CharField(max_length=200, default='* * * * *')

    until = models.DateTimeField(null=True)

    @property
    def deadline_came(self):
        return self.until and self.until < datetime.now()

    def fetch_target_users(self) -> List[User]:
        notification_users_ids = self.groups.all().values_list('users')
        return User.objects.filter(pk__in=notification_users_ids, fcm_token__isnull=False)

    def schedule(self):
        """
        Create notification task with eta = next cron time.
        """
        now = datetime.now()
        croniter_ = croniter(self.frequency, now)
        run_datetime = croniter_.get_next(datetime)
        send_notifications.apply_async((self.pk,), eta=run_datetime)
        return run_datetime
