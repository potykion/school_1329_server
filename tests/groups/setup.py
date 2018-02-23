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

    @pytest.fixture()
    def users_batch_groups(self, users_batch):
        group_1 = Group.objects.create(title='Group with user_1 and user_2')
        group_1.users.add(users_batch[0])
        group_1.users.add(users_batch[1])
        group_1.save()

        group_2 = Group.objects.create(title='Group with user_3 and user_4')
        group_2.users.add(users_batch[2], users_batch[3])
        group_2.save()

        group_3 = Group.objects.create(title='Group with user_5')
        group_3.users.add(users_batch[4])
        group_3.save()

        return [group_1, group_2, group_3]
