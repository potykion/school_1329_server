import pytest
from rest_framework.authtoken.models import Token

from school_1329_server.users.models import User, UserLevel


@pytest.mark.django_db
class UsersFixtures:
    @pytest.fixture()
    def user(self):
        return User.objects.create_user(
            username='potykion',
            password='verysecretpassword',
            level=UserLevel.student
        )

    @pytest.fixture()
    def user_token(self, user):
        token = Token.objects.create(user=user)
        return {'HTTP_AUTHORIZATION': f'Token {token.key}'}

    @pytest.fixture()
    def teacher(self):
        return User.objects.create_user(
            username='galina ivanovna',
            password='verysecretpassword',
            level=UserLevel.teacher
        )

    @pytest.fixture()
    def teacher_token(self, teacher):
        token = Token.objects.create(user=teacher)
        return {'HTTP_AUTHORIZATION': f'Token {token.key}'}

    @pytest.fixture()
    def users_batch(self):
        return [
            User.objects.create_user(username='user_1', password='oppa', level=UserLevel.student, fcm_token='a'),
            User.objects.create_user(username='user_2', password='oppa', level=UserLevel.student, fcm_token='a'),
            User.objects.create_user(username='user_3', password='oppa', level=UserLevel.student, fcm_token='a'),
            User.objects.create_user(username='user_4', password='oppa', level=UserLevel.student, fcm_token='a'),
            User.objects.create_user(username='user_5', password='oppa', level=UserLevel.student, fcm_token='a'),
        ]
