from datetime import datetime, timedelta

import pytest
from django.test import Client

from school_1329_server.users.models import UserLevel, TemporaryPassword, User


@pytest.mark.django_db
class TestUsersViews:

    @pytest.fixture()
    def password(self):
        return TemporaryPassword.objects.create(
            expiration_date=datetime.now() + timedelta(days=1),
            level=1,
            value='opoppaop'
        )

    @pytest.fixture()
    def expired_password(self):
        return TemporaryPassword.objects.create(
            expiration_date=datetime.now() - timedelta(days=1),
            level=1,
            value='opoppaop'
        )

    def test_password_generation(self, client: Client):
        """
        Given expiration date,
        And password level,
        When generate password with given data,
        Then response contains generated password data,
        And new temporary password will be generated.
        """
        expiration_date = datetime(2017, 12, 18, 21, 00)
        password_level = UserLevel.student

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

    def test_password_validation(self, client: Client, password):
        """
        Given temporary unexpired password,
        When validate given password,
        Then response contains info that password is valid.
        """
        response = client.post('/api/users/validate_password', {
            'value': password.value,
            'level': password.level
        })

        assert response.data == {'valid': True}
        assert response.status_code == 200

    def test_validation_of_unexisting_password(self, client: Client, password):
        """
        Given temporary password,
        When validate invalid password,
        Then response contains info that password is invalid.
        """
        response = client.post('/api/users/validate_password', {
            'value': 'aaaaaaaaaa',
            'level': password.level
        })

        assert response.data == {'valid': False}
        assert response.status_code == 400

    def test_validation_of_expired_password(self, client: Client, expired_password):
        """
        Given temporary expired password,
        When validate given password,
        Then response contains info that password is invalid.
        """
        response = client.post('/api/users/validate_password', {
            'value': expired_password.value,
            'level': expired_password.level
        })

        assert response.data == {'valid': False}
        assert response.status_code == 400

    def test_user_creation(self, client: Client, password):
        """
        Given temporary password,
        And username,
        When create user with given password and username,
        Then user is created.
        """
        username = 'pocan'

        response = client.post('/api/users/register', {
            'value': password.value,
            'level': password.level,
            'username': username
        })

        assert response.data == {
            'username': username,
            'level': password.level
        }
        assert User.objects.filter(username=username, level=password.level).exists()

    def test_user_creation_with_expired_password(self, client: Client, expired_password):
        """
        Given expired password,
        And username,
        When create user with given password and username,
        Then response status code is 400.
        """
        username = 'pocan'

        response = client.post('/api/users/register', {
            'value': expired_password.value,
            'level': expired_password.level,
            'username': username
        })

        assert response.status_code == 400
