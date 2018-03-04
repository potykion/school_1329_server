from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from school_1329_server.common.utils import format_time
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
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class ScheduleLesson(models.Model):
    start_time = models.TimeField(verbose_name='Начало')
    end_time = models.TimeField(null=True, verbose_name='Окончание')
    weekday = models.IntegerField(choices=Weekdays.choices, verbose_name='День')

    place = models.CharField(max_length=200, verbose_name='Место проведения')

    subject = models.OneToOneField(ScheduleSubject, models.CASCADE, verbose_name='Предмет')
    teacher = models.ForeignKey(User, models.CASCADE, verbose_name='Учитель')
    groups = models.ManyToManyField(Group, blank=True, verbose_name='Группы')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return (
            f'{Weekdays.get_choice(self.weekday).label} {format_time(self.start_time)} - '
            f'{self.subject} ({self.teacher})'
        )
