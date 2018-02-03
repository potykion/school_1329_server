import pytest

from school_1329_server.groups.models import Group
from tests.users.setup import UsersFixtures


class GroupsFixtures(UsersFixtures):
    @pytest.fixture()
    def group(self):
        return Group.objects.create(title='Sample group')

    @pytest.fixture()
    def group_with_user(self, user):
        group = Group.objects.create(title='Group with user')
        group.users.add(user)
        group.save()
        return group

    @pytest.fixture()
    def groups(self):
        return Group.objects.bulk_create([
            Group(title='Group 1'),
            Group(title='Group 2')
        ])
