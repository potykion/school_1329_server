import pytest

from school_1329_server.notifications.models import Notification
from tests.groups.setup import GroupsFixtures


class NotificationsFixtures(GroupsFixtures):
    @pytest.fixture()
    def sent_notification(self, user, group_with_user):
        notification = Notification.objects.create(
            created_by=user,
            text='Пары не будет!!!',
            sent=True
        )
        notification.groups.add(group_with_user)
        notification.save()
        return notification

    @pytest.fixture()
    def not_sent_notification(self, user, group_with_user):
        notification = Notification.objects.create(
            created_by=user,
            text='Пара будет!!!',
        )
        notification.groups.add(group_with_user)
        notification.save()
        return notification

    @pytest.fixture()
    def notifications(self, sent_notification, not_sent_notification):
        return [
            sent_notification,
            not_sent_notification
        ]

    @pytest.fixture()
    def notification_data(self, group_with_user):
        return {
            'text': 'sample notification',
            'frequency': '* * * * *',
            'send_once': True,
            'groups': [group_with_user.pk],
        }
