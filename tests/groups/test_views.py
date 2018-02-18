from django.test.client import encode_multipart
from rest_framework.response import Response

from school_1329_server.common.utils import datetime_to_drf, encode_data
from school_1329_server.groups.models import Group
from tests.events.setup import EventsFixtures
from tests.groups.setup import GroupsFixtures
from tests.users.setup import UsersFixtures


class TestGroupsViews(EventsFixtures, GroupsFixtures, UsersFixtures):

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

    def test_remove_from_group(self, client, user_token, user, group):
        """
        Given user and group,
        When add user to group,
        And remove user from group,
        Then group contains no users.
        """
        response: Response = client.post(
            f'/api/groups/{group.pk}/add_user',
            **user_token
        )

        response: Response = client.post(
            f'/api/groups/{group.pk}/remove_user',
            **user_token
        )

        assert response.status_code == 200
        assert response.data == {'success': True}
        assert not group.users.filter(pk=user.pk).exists()

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

    def test_create_group(self, client, user_token, user):
        """
        Given group title,
        And token user,
        When create group with given title,
        Then response contains group info,
        And group is created,
        And group contains token-user.
        """
        group_title = 'Sample group 1'

        response: Response = client.post(
            '/api/groups',
            {'title': group_title},
            **user_token
        )

        group = Group.objects.filter(pk=1, title=group_title).first()

        assert response.status_code == 201
        assert response.data == {'id': 1, 'title': group_title}
        assert group.users.filter(pk=user.pk).exists()

    def test_group_update(self, client, user_token, group):
        """
        Given group,
        And new group title,
        When update group,
        Then response is successful,
        And group title equals to given group title.
        """
        group_title = 'Sample group 2'

        encoded_data, content_type = encode_data({'title': group_title})

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

        assert response.status_code == 200
        assert response.data == {'success': True}
        assert not Group.objects.filter(pk=group.pk).exists()

    def test_user_groups(self, client, user_token, user, group):
        """
        Given user and group,
        When add user to group,
        And list user groups,
        Then response contains given group.
        """
        client.post(f'/api/groups/{group.pk}/add_user', **user_token)

        response = client.get('/api/groups/user_groups', **user_token)

        assert response.data == [
            {'id': 1, 'title': group.title}
        ]

    def test_group_users(self, client, user_token, user, group):
        """
        Given user and group,
        When add user to group,
        And list group users,
        Then response contains given user.
        """
        client.post(
            f'/api/groups/{group.pk}/add_user',
            **user_token
        )

        response = client.get(
            f'/api/groups/{group.pk}/users',
            **user_token
        )

        assert response.data == [
            {'username': user.username, 'level': user.level}
        ]

    def test_group_events(
            self, client, user_token,
            event, group_with_user
    ):
        """
        Given group,
        And event with group,
        When list group events,
        Then response contains given event.
        """
        response = client.get(
            f'/api/groups/{group_with_user.pk}/events',
            **user_token
        )

        assert response.data == [
            {
                'id': 1,

                'title': event.title,
                'place': event.place,
                'description': event.description,

                'created_by': event.created_by.username,
                'participation_groups': [group_with_user.pk],

                'start_date': datetime_to_drf(event.start_date),
                'end_date': datetime_to_drf(event.end_date)
            }
        ]
