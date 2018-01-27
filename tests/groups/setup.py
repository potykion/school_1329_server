import pytest

from school_1329_server.groups.models import Group


@pytest.mark.django_db
class GroupsFixtures:
    @pytest.fixture()
    def group(self):
        return Group.objects.create(title='Sample group')

    @pytest.fixture()
    def groups(self):
        return Group.objects.bulk_create([
            Group(title='Group 1'),
            Group(title='Group 2')
        ])
