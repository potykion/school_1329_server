from django.contrib.auth.models import AbstractUser
from django.db import models
from djchoices import DjangoChoices, ChoiceItem


class UserType(DjangoChoices):
    student = ChoiceItem(1)
    teacher = ChoiceItem(2)


class User(AbstractUser):
    """
    Represents user; can be student, teacher or admin.
    """
    # password, email, username are already included

    # null for admins
    type = models.IntegerField(choices=UserType.choices, null=True)


class TemporaryPassword(models.Model):
    """
    Represents temporary password used to authorization in app.
    """
    level = models.IntegerField(choices=UserType.choices)
    expiration_date = models.DateTimeField()
    value = models.CharField(max_length=32)
