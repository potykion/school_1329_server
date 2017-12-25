from datetime import datetime, timedelta

import pytest
from django.test import Client
from django.utils import timezone
from pytz import UTC

from school_1329_server.users.models import UserLevel, TemporaryPassword, User


@pytest.mark.django_db
class TestUsersViews:

    @pytest.fixture()
    def password(self):
        return TemporaryPassword.objects.create(
            expiration_date=timezone.now() + timedelta(days=1),
            level=1,
            password_value='opoppaop'
        )

    @pytest.fixture()
    def expired_password(self):
        return TemporaryPassword.objects.create(
            expiration_date=timezone.now() - timedelta(days=1),
            level=1,
            password_value='opoppaop'
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
        password_level = UserLevel.student

        response = client.post('/api/users/generate_password', {
            'expiration_date': expiration_date,
            'level': password_level
        })

        assert response.data == {
            'expiration_date': expiration_date.isoformat()[:-6] + 'Z',
            'level': password_level,
            # password value is random
            'password_value': response.data['password_value']
        }
        assert TemporaryPassword.objects.filter(expiration_date=expiration_date, level=password_level).exists()

    def test_password_validation(self, client: Client, password):
        """
        Given temporary unexpired password,
        When validate given password,
        Then response contains info that password is valid.
        """
        response = client.post('/api/users/validate_password', {
            'password_value': password.password_value,
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
            'password_value': 'aaaaaaaaaa',
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
            'password_value': expired_password.password_value,
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
            'password_value': password.password_value,
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
            'password_value': expired_password.password_value,
            'level': expired_password.level,
            'username': username
        })

        assert response.status_code == 400

    def test_teacher_admin_password_generation(self, client: Client):
        """
        Given teacher,
        When generate admin password,
        Then response contains generated password,
        And teacher has generated password.
        """
        teacher = User.objects.create(username='ychitel', level=UserLevel.teacher)

        response = client.post('/api/users/generate_admin_password', {
            'username': teacher.username
        })

        assert response.data == {
            'password_value': response.data['password_value']
        }
        assert User.objects.get(pk=teacher.pk).password == response.data['password_value']

    def test_teacher_admin_password_generation_if_user_is_student(self, client: Client):
        """
        Given student,
        When generate admin password,
        Then response status is 403,
        And student has no generated password.
        """
        student = User.objects.create(username='stydentiwka', level=UserLevel.student)

        response = client.post('/api/users/generate_admin_password', {
            'username': student.username
        })

        assert response.status_code == 403
        assert not User.objects.get(pk=student.pk).password
