from django.contrib.auth.models import AbstractUser
from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from school_1329_server.users.utils import generate_password


class UserLevel(DjangoChoices):
    admin = ChoiceItem(0)
    student = ChoiceItem(1)
    teacher = ChoiceItem(2)


class User(AbstractUser):
    """
    Represents user; can be student, teacher or admin.
    """
    # password, email, username are already included

    # null for admins
    level = models.IntegerField(choices=UserLevel.choices, default=0)

    def generate_password(self):
        password = generate_password()
        self.password = password
        self.save()
        return password


class TemporaryPassword(models.Model):
    """
    Represents temporary password used to authorization in app.
    """
    level = models.IntegerField(choices=UserLevel.choices)
    expiration_date = models.DateTimeField()
    value = models.CharField(max_length=32)
