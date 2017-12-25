import pytest

from school_1329_server.users.models import User


@pytest.mark.django_db
class UsersFixtures:
    @pytest.fixture()
    def user(self):
        return User.objects.create_user(
            username='potykion',
            password='verysecretpassword'
        )
