import pytest

from school_1329_server.schedule.models import ScheduleSubject, ScheduleLesson, Weekdays
from tests.groups.setup import GroupsFixtures


class ScheduleFixtures(GroupsFixtures):
    @pytest.fixture()
    def subject(self):
        return ScheduleSubject.objects.create(title='Русский')

    @pytest.fixture()
    def schedule_item(self, teacher, subject, group_with_user):
        item = ScheduleLesson.objects.create(
            teacher=teacher,
            subject=subject,
            start_time='12:00',
            weekday=Weekdays.Monday
        )
        item.groups.add(group_with_user)
        item.save()
        return item

    @pytest.fixture()
    def schedule_item_data(self, subject, group_with_user):
        return {
            'subject': subject.pk,
            'groups': [group_with_user.pk],
            'start_time': '12:00',
            'weekday': 1
        }
