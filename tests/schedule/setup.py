import pytest

from school_1329_server.schedule.models import ScheduleSubject


@pytest.mark.django_db
class ScheduleFixtures:
    @pytest.fixture()
    def subject(self):
        return ScheduleSubject.objects.create(title='Русский')
