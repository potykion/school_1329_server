from django.test.client import encode_multipart
from rest_framework.response import Response

from school_1329_server.groups.models import Group
from tests.groups.setup import GroupsFixtures
from tests.users.setup import UsersFixtures


class TestGroupsViews(GroupsFixtures, UsersFixtures):

    def test_add_to_group(self, client, user, group, user_token):
        """
        Given user and group,
        When add user to group,
        Then response is success.
        And user is added to group,
        """
        response: Response = client.post(
            f'/api/groups/{group.pk}/add_user',
            **user_token
        )

        assert response.status_code == 200
        assert response.data == {'success': True}
        assert group.users.filter(pk=user.pk).exists()

    def test_groups_list(self, client, user_token, groups):
        """
        Given groups,
        When list groups,
        Then response contains list of groups.
        """
        response: Response = client.get(
            '/api/groups',
            **user_token
        )

        assert response.data == [
            {'id': 1, 'title': 'Group 1'},
            {'id': 2, 'title': 'Group 2'}
        ]

    def test_create_group(self, client, user_token):
        """
        Given group title,
        When create group with given title,
        Then response contains group info,
        And group is created.
        """
        group_title = 'Sample group 1'

        response: Response = client.post(
            '/api/groups',
            {'title': group_title},
            **user_token
        )

        assert response.status_code == 201
        assert response.data == {'id': 1, 'title': group_title}
        assert Group.objects.filter(pk=1, title=group_title).exists()

    def test_group_update(self, client, user_token, group):
        """
        Given group,
        And new group title,
        When update group,
        Then response is successful,
        And group title equals to given group title.
        """
        group_title = 'Sample group 2'

        boundary_string = 'BoUnDaRyStRiNg'
        encoded_data = encode_multipart(boundary_string, {'title': group_title})
        content_type = f'multipart/form-data; boundary={boundary_string}'

        response: Response = client.put(
            f'/api/groups/{group.pk}',
            encoded_data,
            **user_token,
            content_type=content_type
        )

        assert response.status_code == 200
        assert Group.objects.get(pk=group.pk).title == group_title

    def test_group_delete(self, client, user_token, group):
        """
        Given group,
        When delete group,
        Then response is successful,
        And no group exists.
        """
        response: Response = client.delete(f'/api/groups/{group.pk}', **user_token)

        assert response.status_code == 204
        assert not Group.objects.filter(pk=group.pk).exists()
