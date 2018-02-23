from school_1329_server.notifications.models import Notification
from tests.notifications.setup import NotificationsFixtures


class TestNotificationsModels(NotificationsFixtures):
    def test_users_fetch(self, users_batch_groups, users_batch, user):
        """
        Given bunch of groups,
        And user,
        When create notification,
        And fetch notification users,
        Then notification users count equal to number of users in all groups.
        """
        notification = Notification.objects.create(created_by=user, text='a')
        notification.groups.add(*users_batch_groups)
        users = notification.fetch_target_users()

        assert users.count() == len(users_batch)
