from django.contrib import admin
from django.contrib.auth.models import Group as AuthGroup
from fcm_django.models import FCMDevice
from rest_framework.authtoken.models import Token

from school_1329_server.events.models import Event, EventComment
from school_1329_server.notifications.models import Notification
from school_1329_server.schedule.models import ScheduleSubject, ScheduleLesson, ScheduleTeacher
from school_1329_server.users.models import User, RegistrationCode
from school_1329_server.groups.models import Group


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = (
        'last_login', 'is_superuser', 'groups', 'is_active', 'email',
        'first_name', 'last_name', 'is_staff', 'date_joined',
        'user_permissions', 'password',
        'fcm_token',
    )


admin.site.unregister([
    AuthGroup, Token, FCMDevice
])
admin.site.register([
    Group, RegistrationCode,
    Event, EventComment,
    ScheduleSubject, ScheduleLesson, ScheduleTeacher,
    Notification
])
admin.site.index_template = 'general/custom_admin.html'
admin.site.site_url = ''
admin.site.index_title = 'Администрирование приложения'
admin.site.site_header = 'Администрирование приложения'
