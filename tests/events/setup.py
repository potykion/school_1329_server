import pytest
from datetime import datetime, time

import pytz
from django.utils import timezone

from school_1329_server.events.models import Event
from tests.groups.setup import GroupsFixtures
from tests.users.setup import UsersFixtures


class EventsFixtures(GroupsFixtures, UsersFixtures):

    @pytest.fixture()
    def event_data(self, group):
        return {
            'title': 'Event 1',
            'place': 'Sch1329',
            'participation_groups': [group.pk],
            'start_date': datetime.combine(
                timezone.now().date(),
                time(12, 00, tzinfo=pytz.UTC)
            )
        }

    @pytest.fixture
    def event(self, user, group):
        event = Event.objects.create(
            title='Линейка',
            place='Школка',
            description='Чисто собраться',

            created_by=user,

            start_date=datetime.now()
        )

        event.participation_groups.add(*[group])
        event.save()

        return event
