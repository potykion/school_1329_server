from django.db import models

from school_1329_server.users.models import User


class Group(models.Model):
    title = models.CharField(max_length=60)
    users = models.ManyToManyField(User)
