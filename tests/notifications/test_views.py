from school_1329_server.common.utils import encode_data, datetime_to_drf
from school_1329_server.notifications.models import Notification
from tests.notifications.setup import NotificationsFixtures


class TestNotificationsViews(NotificationsFixtures):
    def test_list_sent_notifications(
            self, client, user_token,
            notifications
    ):
        """
        Given notifications (sent and not sent),
        When fetch sent notifications,
        Then response contains only sent notifications related to user.
        """
        response = client.get(
            '/api/notifications/list_sent_notifications',
            **user_token
        )

        assert response.data[0] == {
            'id': 1,
            'text': 'Пары не будет!!!',
            'created_by': 'potykion',
            'frequency': '* * * * *',
            'groups': [1],
            'send_once': True,
            'until': None
        }

    def test_list_created_notifications(
            self, client, user_token,
            notifications, user
    ):
        """
        Given notifications (sent and not sent),
        And user,
        When fetch notifications created by user,
        Then response contains only notifications created by user.
        """
        response = client.get(
            '/api/notifications/list_created_notifications',
            **user_token
        )

        assert len(response.data) == 2
        assert response.data[0] == {
            'id': 1,
            'text': 'Пары не будет!!!',
            'send_once': True,
            'groups': [1],
            'frequency': '* * * * *',
            'created_by': 'potykion',
            'until': None
        }

    def test_create_notification(
            self, client, user_token,
            notification_data
    ):
        """
        Given notification data,
        When create notification with given data,
        Then notification is created,
        And response contains notification data.
        """
        response = client.post(
            '/api/notifications',
            notification_data,
            **user_token
        )

        notification = Notification.objects.get()
        assert response.data == {
            'id': notification.pk,
            'text': notification_data['text'],
            'frequency': notification_data['frequency'],
            'send_once': notification_data['send_once'],
            'groups': notification_data['groups'],
            'created_by': 'potykion',
            'until': datetime_to_drf(notification.until)
        }

    def test_alter_notification(
            self, client, user_token,
            sent_notification, notification_data
    ):
        """
        Given notification,
        And altered notification data,
        When update notification,
        Then notification is updated.
        """
        notification_data['send_once'] = False

        encoded_data, content_type = encode_data(notification_data)
        response = client.put(
            f'/api/notifications/{sent_notification.pk}',
            encoded_data,
            content_type=content_type,
            **user_token
        )

        notification = Notification.objects.get(pk=sent_notification.pk)
        assert not notification.send_once
        assert response.data == {
            'id': notification.pk,
            'text': notification_data['text'],
            'frequency': notification_data['frequency'],
            'send_once': notification_data['send_once'],
            'groups': notification_data['groups'],
            'created_by': 'potykion',
            'until': datetime_to_drf(notification.until)
        }
