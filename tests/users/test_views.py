from datetime import datetime

import pytest
from django.test import Client

from school_1329_server.users.models import UserType, TemporaryPassword


@pytest.mark.django_db
def test_password_generation(client: Client):
    """
    Given expiration date,
    And password level,
    When generate password with given data,
    Then response contains generated password data,
    And new temporary password will be generated.
    """
    expiration_date = datetime(2017, 12, 18, 21, 00)
    password_level = UserType.student

    response = client.post('/api/users/generate_password', {
        'expiration_date': expiration_date,
        'level': password_level
    })

    assert response.data == {
        'expiration_date': expiration_date.isoformat() + 'Z',
        'level': password_level,
        # password value is random
        'value': response.data['value']
    }
    assert TemporaryPassword.objects.filter(expiration_date=expiration_date, level=password_level).exists()
