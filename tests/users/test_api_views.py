from datetime import datetime, timedelta

import pytest
from django.test import Client
from django.utils import timezone
from pytz import UTC

from school_1329_server.users.models import UserLevel, RegistrationCode, User


@pytest.mark.django_db
class TestUsersViews:

    @pytest.fixture()
    def registration_code(self):
        return RegistrationCode.objects.create(
            expiration_date=timezone.now() + timedelta(days=1),
            level=1,
            code='opoppaop'
        )

    def test_password_generation(self, client: Client):
        """
        Given expiration date,
        And password level,
        When generate password with given data,
        Then response contains generated password data,
        And new temporary password will be generated.
        """
        expiration_date = timezone.now() + timedelta(days=2)
        level = UserLevel.student

        response = client.post('/api/users/create_code', {
            'expiration_date': expiration_date,
            'level': level
        })

        assert response.data == {
            'code': response.data['code']
        }
        assert RegistrationCode.objects.filter(
            expiration_date=expiration_date,
            level=level
        ).exists()

    @pytest.fixture()
    def expired_registration_code(self):
        return RegistrationCode.objects.create(
            expiration_date=timezone.now() - timedelta(days=1),
            level=1,
            code='opoppaop'
        )

    def test_password_validation(self, client: Client, registration_code):
        """
        Given temporary unexpired password,
        When validate given password,
        Then response contains info that password is valid.
        """
        response = client.post('/api/users/check_code', {
            'code': registration_code.code,
            'level': registration_code.level
        })

        assert response.data == {'correct': True}
        assert response.status_code == 200

    def test_validation_of_unexisting_password(self, client: Client, registration_code):
        """
        Given temporary password,
        When validate invalid password,
        Then response contains info that password is invalid.
        """
        response = client.post('/api/users/check_code', {
            'code': 'aaaaaaaaaa',
            'level': registration_code.level
        })

        assert response.data == {'correct': False}
        assert response.status_code == 400

    def test_validation_of_expired_password(self, client: Client, expired_registration_code):
        """
        Given temporary expired password,
        When validate given password,
        Then response contains info that password is invalid.
        """
        response = client.post('/api/users/check_code', {
            'code': expired_registration_code.code,
            'level': expired_registration_code.level
        })

        assert response.data == {'correct': False}
        assert response.status_code == 400

    def test_user_creation(self, client: Client, registration_code):
        """
        Given temporary password,
        And username,
        When create user with given password and username,
        Then user is created.
        """
        username = 'pocan'

        response = client.post('/api/users/register', {
            'code': registration_code.code,
            'level': registration_code.level,
            'username': username
        })

        assert response.data == {
            'username': username,
            'level': registration_code.level
        }
        assert User.objects.filter(username=username, level=registration_code.level).exists()

    def test_user_creation_with_expired_password(self, client: Client, expired_registration_code):
        """
        Given expired password,
        And username,
        When create user with given password and username,
        Then response status code is 400.
        """
        username = 'pocan'

        response = client.post('/api/users/register', {
            'code': expired_registration_code.code,
            'level': expired_registration_code.level,
            'username': username
        })

        assert response.status_code == 400
