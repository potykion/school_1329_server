from django.db import models

from school_1329_server.groups.models import Group
from school_1329_server.users.models import User


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    place = models.CharField(max_length=200, verbose_name='Место проведения')
    description = models.TextField(blank=True, verbose_name='Описание')

    participation_groups = models.ManyToManyField(Group, blank=True, verbose_name='Группы-участники')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создано')

    start_date = models.DateTimeField(verbose_name='Начало')
    end_date = models.DateTimeField(null=True, verbose_name='Окончание')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f'{self.title}'


class EventComment(models.Model):
    text = models.TextField(verbose_name='Текст')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создано')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments', verbose_name='Мероприятие')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.event}: {self.text}'
