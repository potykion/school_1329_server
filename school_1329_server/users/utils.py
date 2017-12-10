import string
import random


def generate_password(length=8):
    """
    Generate random password with given length.
    :param length: Password length.
    :return: Password with given length.
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))
