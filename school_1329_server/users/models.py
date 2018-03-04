from django.contrib.auth.models import AbstractUser
from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from school_1329_server.users.utils import generate_registration_code, generate_expiration_date


class UserLevel(DjangoChoices):
    admin = ChoiceItem(0, label='Администратор')
    student = ChoiceItem(1, label='Ученик')
    teacher = ChoiceItem(2, label='Учитель')


class User(AbstractUser):
    """
    Represents user; can be student, teacher or admin.
    Password, email, username are already included
    """

    level = models.IntegerField(choices=UserLevel.choices, default=0, verbose_name='Уровень')

    fcm_token = models.CharField(max_length=200, null=True)


class RegistrationCode(models.Model):
    """
    Represents temporary password used to authorization in app.
    """
    level = models.IntegerField(
        choices=UserLevel.choices, default=UserLevel.teacher,
        verbose_name='Уровень'
    )

    expiration_date = models.DateTimeField(default=generate_expiration_date, verbose_name='Срок годности')
    code = models.CharField(max_length=32, default=generate_registration_code, verbose_name='Код')

    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name_plural = 'Коды регистрации'
        verbose_name = 'Код регистрации'

    def __str__(self):
        return f'{self.code}'
