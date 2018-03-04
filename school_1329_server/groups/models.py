from django.db import models

from school_1329_server.users.models import User


class Group(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    users = models.ManyToManyField(User, verbose_name='Участники')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f'{self.title}'
