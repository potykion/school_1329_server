from datetime import timedelta

from django.utils import timezone

from school_1329_server.common.utils import datetime_to_drf, encode_data
from school_1329_server.events.models import Event
from tests.events.setup import EventsFixtures


class TestEventsViews(EventsFixtures):
    def test_event_creation(
            self, client, user_token,
            user, group, event_data
    ):
        """
        Given user and group,
        And event data.
        When create event,
        Then response contains event info,
        And event is created.
        """
        response = client.post(
            '/api/events',
            event_data,
            **user_token
        )

        assert response.data == {
            **event_data,
            'id': 1,

            'description': '',

            'created_by': user.username,

            'start_date': datetime_to_drf(event_data['start_date']),
            'end_date': None,
        }
        assert Event.objects.filter(title=event_data['title']).exists()

    def test_event_list(
            self, client, user_token,
            event,
            user, group_with_user
    ):
        """
        Given event,
        When list events,
        Then response contains list of all events.
        """
        response = client.get(
            '/api/events',
            **user_token
        )

        assert response.data == [
            {
                'id': 1,

                'title': event.title,
                'place': event.place,
                'description': event.description,

                'created_by': user.username,
                'participation_groups': [group_with_user.pk],

                'start_date': datetime_to_drf(event.start_date),
                'end_date': None
            }
        ]

    def test_event_update(
            self, client, user_token,
            event,
            user, group
    ):
        """
        Given event,
        And new event data
        When update event data,
        Then response contains updated event,
        And event is updated.
        """
        start_date = timezone.now() + timedelta(days=2)
        end_date = start_date + timedelta(hours=2)
        new_event_data = {
            'title': event.title,
            'place': 'Ne wkola',
            'description': event.description,

            'participation_groups': [],

            'start_date': start_date,
            'end_date': end_date,
        }

        encoded_data, content_type = encode_data(new_event_data)

        response = client.put(
            f'/api/events/{event.pk}',
            encoded_data,
            **user_token,
            content_type=content_type
        )

        assert response.data == {
            'id': 1,

            'title': event.title,
            'place': 'Ne wkola',
            'description': event.description,

            'created_by': user.username,
            'participation_groups': [],

            'start_date': datetime_to_drf(start_date),
            'end_date': datetime_to_drf(end_date)
        }

    def test_event_delete(
            self, client, user_token,
            event,
    ):
        """
        Given event,
        When delete event,
        Ther response contains success,
        And no event exists.
        """
        response = client.delete(
            f'/api/events/{event.pk}',
            **user_token
        )

        assert response.status_code == 200
        assert response.data == {'success': True}
        assert not Event.objects.filter(pk=event.pk).exists()

    def test_user_entered_events(
            self, client, user_token,
            event, user, group_with_user
    ):
        """
        Given event and user,
        When fetch user events,
        Then response contains user events.
        """
        response = client.get('/api/events/user_entered_events', **user_token)

        assert len(response.data) == 1
        assert response.data[0] == {
            'id': 1,

            'title': event.title,
            'place': event.place,
            'description': event.description,

            'created_by': user.username,
            'participation_groups': [group_with_user.pk],

            'start_date': datetime_to_drf(event.start_date),
            'end_date': datetime_to_drf(event.end_date)
        }

    def test_user_created_events(
            self, client, user_token,
            event, user
    ):
        """
        Given user and event,
        When fetch events created by user,
        Then response contains created by user events.
        """
        response = client.get('/api/events/user_created_events', **user_token)

        assert len(response.data)
        assert response.data[0] == {
            'id': 1,

            'title': event.title,
            'place': event.place,
            'description': event.description,

            'created_by': user.username,
            'participation_groups': list(event.participation_groups.values_list('pk', flat=True)),

            'start_date': datetime_to_drf(event.start_date),
            'end_date': datetime_to_drf(event.end_date)
        }

    def test_events_csv_view(self, client, user_token, event):
        """
        Given events,
        When fetch events in CSV format,
        Then response contains events in CSV format.
        """
        response = client.get('/api/events/csv', **user_token)

        event_groups_str = ','.join(map(str, event.participation_groups.values_list('id', flat=True)))
        event_end_date = datetime_to_drf(event.end_date) or ''
        event_start_date = datetime_to_drf(event.start_date) or ''

        response_content = response.content.decode('utf-8')
        assert response_content == (
            'created_by,description,end_date,id,participation_groups.0,place,start_date,title\r\n'
            f'{event.created_by.username},{event.description},{event_end_date},{event.id},{event_groups_str},{event.place},{event_start_date},{event.title}\r\n'
        )
