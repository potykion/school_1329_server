from django.db import models

from school_1329_server.groups.models import Group
from school_1329_server.users.models import User


class Event(models.Model):
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    participation_groups = models.ManyToManyField(Group, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)

# class EventComment(models.Model):
#     text = models.TextField()
#
#     created_by = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     created = models.DateTimeField(auto_now_add=True)
