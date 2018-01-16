import string
import random
from datetime import timedelta

from django.utils import timezone


def generate_registration_code(length=8):
    """
    Generate random password with given length.
    :param length: Password length.
    :return: Password with given length.
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))


def generate_expiration_date(days=7):
    return timezone.now() + timedelta(days=days)
