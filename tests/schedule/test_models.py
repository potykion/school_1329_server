import os

import pytest

from config.settings.common import STATIC_ROOT
from school_1329_server.groups.models import Group
from school_1329_server.schedule.models import ScheduleLesson, ScheduleTeacher, ScheduleSubject


class TestScheduleLessonManager:
    @pytest.mark.django_db
    def test_create_from_json(self):
        """
        Given lessons json,
        When create lessons from json,
        Then lessons created along with groups, teachers and subjects.
        """
        lessons_json = os.path.join(STATIC_ROOT, 'schedule.json')

        ScheduleLesson.objects.create_from_json(lessons_json)

        assert ScheduleLesson.objects.count() == 28
        assert ScheduleTeacher.objects.count() == 7
        assert ScheduleSubject.objects.count() == 13
        assert Group.objects.count() == 3
