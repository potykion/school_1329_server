from datetime import datetime, timedelta

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


@pytest.mark.django_db
def test_password_validation(client: Client):
    """
    Given temporary unexpired password,
    When validate given password,
    Then response contains info that password is valid.
    """
    password = TemporaryPassword.objects.create(
        expiration_date=datetime.now() + timedelta(days=1),
        level=1,
        value='opoppaop'
    )

    response = client.post('/api/users/validate_password', {
        'value': password.value,
        'level': password.level
    })

    assert response.data == {'valid': True}
    assert response.status_code == 200


@pytest.mark.django_db
def test_validation_of_unexisting_password(client: Client):
    """
    Given temporary password,
    When validate invalid password,
    Then response contains info that password is invalid.
    """
    password = TemporaryPassword.objects.create(
        expiration_date=datetime.now() + timedelta(days=1),
        level=1,
        value='opoppaop'
    )

    response = client.post('/api/users/validate_password', {
        'value': 'aaaaaaaaaa',
        'level': password.level
    })

    assert response.data == {'valid': False}
    assert response.status_code == 400


@pytest.mark.django_db
def test_validation_of_expired_password(client: Client):
    """
    Given temporary expired password,
    When validate given password,
    Then response contains info that password is invalid.
    """
    password = TemporaryPassword.objects.create(
        expiration_date=datetime.now() - timedelta(days=1),
        level=1,
        value='opoppaop'
    )

    response = client.post('/api/users/validate_password', {
        'value': password.value,
        'level': password.level
    })

    assert response.data == {'valid': False}
    assert response.status_code == 400
