from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from school_1329_server.groups.models import Group
from school_1329_server.users.models import User


class Weekdays(DjangoChoices):
    Monday = ChoiceItem(1, 'Понедельник')
    Tuesday = ChoiceItem(2, 'Вторник')
    Wednesday = ChoiceItem(3, 'Среда')
    Thursday = ChoiceItem(4, 'Четверг')
    Friday = ChoiceItem(5, 'Пятница')
    Saturday = ChoiceItem(6, 'Суббота')
    Sunday = ChoiceItem(7, 'Воскресенье')


class ScheduleSubject(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ScheduleLesson(models.Model):
    start_time = models.TimeField()
    weekday = models.IntegerField(choices=Weekdays.choices)

    subject = models.OneToOneField(ScheduleSubject, models.CASCADE)
    teacher = models.OneToOneField(User, models.CASCADE)
    groups = models.ManyToManyField(Group, blank=True)
