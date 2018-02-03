from operator import attrgetter

from school_1329_server.common.utils import encode_data
from school_1329_server.schedule.models import ScheduleLesson
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

    def test_create_schedule_item(
            self, client, teacher_token,
            schedule_item_data, teacher
    ):
        """
        Given schedule item data (group, teacher, start time, weekday, subject),
        And teacher,
        When create schedule item,
        Then schedule item is created,
        And response contains schedule item info.
        """
        response = client.post(
            '/api/schedule_lessons',
            data=schedule_item_data,
            **teacher_token
        )

        item = ScheduleLesson.objects.get()
        assert item.pk
        assert response.data == {**schedule_item_data, 'teacher': teacher.username, 'id': item.pk}

    def test_update_schedule_item(
            self, client, teacher_token,
            schedule_item, teacher
    ):
        """
        Given schedule item,
        And new schedule data,
        When update schedule item,
        Then schedule item is updated,
        And response contains new schedule data.
        """
        new_schedule_data = {
            'place': 'wkola2',
            'start_time': '13:00',
            'weekday': 2,
            'subject': schedule_item.subject.pk,
            'groups': list(schedule_item.groups.values_list('pk', flat=True)),
        }

        encoded_data, content_type = encode_data(new_schedule_data)

        response = client.put(
            f'/api/schedule_lessons/{schedule_item.pk}',
            encoded_data,
            **teacher_token,
            content_type=content_type
        )

        item = ScheduleLesson.objects.get(pk=schedule_item.pk)
        assert str(item.start_time)[:-3] == '13:00'
        assert response.data == {
            'id': item.pk,
            'teacher': teacher.username,

            'place': new_schedule_data['place'],
            'groups': new_schedule_data['groups'],
            'start_time': new_schedule_data['start_time'],
            'subject': new_schedule_data['subject'],
            'weekday': new_schedule_data['weekday']
        }

    def test_delete_schedule_item(
            self, client, teacher_token,
            schedule_item
    ):
        """
        Given schedule item,
        When delete schedule item,
        Then schedule item is deleted.
        """
        response = client.delete(
            f'/api/schedule_lessons/{schedule_item.pk}',
            **teacher_token
        )

        assert not ScheduleLesson.objects.filter(pk=schedule_item.pk).exists()
