from school_1329_server.common.utils import datetime_to_drf
from school_1329_server.events.models import EventComment
from tests.events.setup import EventsFixtures, EventCommentsFixtures


class TestEventCommentsViews(EventCommentsFixtures):
    def test_event_comments_list(
            self, client, user_token,
            event, event_comments, user
    ):
        """
        Given event,
        And event comments,
        When list event comments,
        Then response contains event comments.
        """
        response = client.get(
            '/api/event_comments', {'event': event.id},
            **user_token
        )

        assert response.data == [
            {
                'id': 1,
                'text': 'op',
                'created_by': user.username,
                'created': datetime_to_drf(event_comments[0].created)
            },
            {
                'id': 2,
                'text': 'oppa',
                'created_by': user.username,
                'created': datetime_to_drf(event_comments[1].created)
            },
            {
                'id': 3,
                'text': 'op oppa',
                'created_by': user.username,
                'created': datetime_to_drf(event_comments[2].created)
            },
        ]

    def test_event_comments_receive_via_query_parameter(
            self, client, user_token,
            event_comments, event
    ):
        """
        Given event comments and event,
        When list event comments by passing event id as query parameter,
        And list event comments by passing event id as body field,
        Then request with query parameter response data equals to second request data.
        """
        query_request_response = client.get(f'/api/event_comments?event={event.pk}', **user_token)
        body_request_response = client.get('/api/event_comments', {'event': event.pk}, **user_token)

        assert query_request_response.data == body_request_response.data

    def test_event_comment_creation(
            self, client, user_token,
            event, user
    ):
        """
        Given event and user,
        And comment text,
        When create comment for given event,
        Then response contains comment data,
        And comment is created.
        """
        comment_text = 'sample text'
        response = client.post(
            '/api/event_comments',
            {
                'event': event.id,
                'text': comment_text
            },
            **user_token
        )

        commment = EventComment.objects.get(text=comment_text)

        assert response.data == {
            'id': 1,
            'created_by': user.username,
            'text': comment_text,
            'created': datetime_to_drf(commment.created)
        }

    def test_event_comment_deletion(
            self, client, user_token,
            event_comments,
    ):
        """
        Given event comments,
        And id of comment to delete,
        When delete comment with given id,
        Then response is successful,
        And no comment with id exists.
        """
        comment_id = event_comments[0].id

        response = client.delete(
            f'/api/event_comments/{comment_id}',
            **user_token
        )

        assert response.data == {'success': True}
        assert not EventComment.objects.filter(pk=comment_id).exists()
