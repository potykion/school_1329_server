import pytest
from datetime import datetime, time

import pytz
from django.utils import timezone

from school_1329_server.events.models import Event, EventComment
from tests.groups.setup import GroupsFixtures
from tests.users.setup import UsersFixtures


class EventsFixtures(GroupsFixtures, UsersFixtures):

    @pytest.fixture()
    def event_data(self, group_with_user):
        return {
            'title': 'Event 1',
            'place': 'Sch1329',
            'participation_groups': [group_with_user.pk],
            'start_date': datetime.combine(
                timezone.now().date(),
                time(12, 00, tzinfo=pytz.UTC)
            )
        }

    @pytest.fixture
    def event(self, user, group_with_user):
        event = Event.objects.create(
            title='Линейка',
            place='Школка',
            description='Чисто собраться',

            created_by=user,

            start_date=datetime.now()
        )

        event.participation_groups.add(group_with_user)
        event.save()

        return event


class EventCommentsFixtures(EventsFixtures):
    @pytest.fixture()
    def event_comments(self, user, event):
        return EventComment.objects.bulk_create([
            EventComment(id=1, created_by=user, event=event, text='op'),
            EventComment(id=2, created_by=user, event=event, text='oppa'),
            EventComment(id=3, created_by=user, event=event, text='op oppa'),
        ])
