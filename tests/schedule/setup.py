import os
import pytest

from config.settings.common import STATIC_ROOT
from school_1329_server.schedule.models import ScheduleSubject, ScheduleLesson, Weekdays, ScheduleTeacher
from tests.groups.setup import GroupsFixtures


class ScheduleFixtures(GroupsFixtures):
    @pytest.fixture()
    def subject(self):
        return ScheduleSubject.objects.create(title='Русский')

    @pytest.fixture()
    def schedule_item(self, teacher, subject, group_with_user):
        teacher = ScheduleTeacher.objects.create(name=teacher.username)
        item = ScheduleLesson.objects.create(
            teacher=teacher,
            subject=subject,
            start_time='12:00',
            end_time='12:45',
            weekday=Weekdays.Monday,
            place='wkola'
        )
        item.groups.add(group_with_user)
        item.save()
        return item

    @pytest.fixture()
    def schedule_item_data(self, subject, group_with_user):
        return {
            'subject': subject.pk,
            'groups': [group_with_user.pk],
            'place': 'wkola',
            'start_time': '12:00',
            'weekday': 1
        }

    @pytest.fixture()
    def week_schedule(self):
        lessons_json = os.path.join(STATIC_ROOT, 'schedule.json')
        ScheduleLesson.objects.create_from_json(lessons_json)
        return ScheduleLesson.objects.all()
