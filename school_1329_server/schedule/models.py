from django.db import models


class ScheduleSubject(models.Model):
    title = models.CharField(max_length=200)
