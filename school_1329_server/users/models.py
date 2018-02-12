from django.contrib.auth.models import AbstractUser
from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from school_1329_server.users.utils import generate_registration_code, generate_expiration_date


class UserLevel(DjangoChoices):
    admin = ChoiceItem(0)
    student = ChoiceItem(1)
    teacher = ChoiceItem(2)


class User(AbstractUser):
    """
    Represents user; can be student, teacher or admin.
    """
    # password, email, username are already included

    level = models.IntegerField(choices=UserLevel.choices, default=0)


class RegistrationCode(models.Model):
    """
    Represents temporary password used to authorization in app.
    """
    level = models.IntegerField(choices=UserLevel.choices, default=UserLevel.teacher)

    expiration_date = models.DateTimeField(default=generate_expiration_date)
    code = models.CharField(max_length=32, default=generate_registration_code)

    date_created = models.DateTimeField(auto_now_add=True)
