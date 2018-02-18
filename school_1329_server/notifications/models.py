from django.db import models

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
