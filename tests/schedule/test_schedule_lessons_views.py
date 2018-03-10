from operator import attrgetter

from school_1329_server.common.utils import encode_data, format_time
from school_1329_server.schedule.models import ScheduleLesson
from school_1329_server.schedule.utils import compute_end_time
from tests.schedule.setup import ScheduleFixtures
from tests.users.setup import UsersFixtures


class TestScheduleItemsViews(ScheduleFixtures, UsersFixtures):
    def test_user_schedule(
            self, client, user_token,
            user, schedule_item
    ):
        """
        Given user,
        And schedule items,
        When list user schedule,
        Then response contains user schedule.
        """
        response = client.get(
            '/api/schedule_lessons/user_schedule',
            **user_token
        )

        assert response.data == {
            1: [
                {
                    'id': 1,
                    'start_time': '12:00',
                    'end_time': '12:45',
                    'subject': 'Русский',
                    'teacher': 'galina ivanovna',
                    'place': 'wkola'
                }
            ],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: []
        }

