from django.contrib import admin
from django.contrib.auth.models import Group as AuthGroup
from rest_framework.authtoken.models import Token

from school_1329_server.events.models import Event, EventComment
from school_1329_server.schedule.models import ScheduleSubject
from school_1329_server.users.models import User, RegistrationCode
from school_1329_server.groups.models import Group

admin.site.unregister([
    AuthGroup, Token
])
admin.site.register([
    User, Group, RegistrationCode, Event, EventComment, ScheduleSubject
])
