from datetime import datetime
from typing import List

from croniter import croniter
from django.db import models

from school_1329_server.common.tasks import send_notifications
from school_1329_server.groups.models import Group
from school_1329_server.users.models import User


class Notification(models.Model):
    text = models.TextField(verbose_name='Текст')

    created_by = models.ForeignKey(User, models.CASCADE, verbose_name='Создано')
    groups = models.ManyToManyField(Group, verbose_name='Группы')

    sent = models.BooleanField(default=False, verbose_name='Отправлено')
    send_once = models.BooleanField(default=True, verbose_name='Отправить один раз')

    # crontab mask: https://crontab.guru/
    frequency = models.CharField(
        max_length=200, default='* * * * *', verbose_name='Частота',
        help_text='Частота в формате crontab (https://ru.wikipedia.org/wiki/Cron#crontab)'
    )

    until = models.DateTimeField(null=True, verbose_name='Срок отправки')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Уведомления'
        verbose_name = 'Уведомление'

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

    def __str__(self):
        return f'{self.text}'
