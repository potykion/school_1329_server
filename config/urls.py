"""school_1329_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from school_1329_server.events.views import EventsViewSet, EventCommentsViewSet
from school_1329_server.groups.views import GroupsViewSet
from school_1329_server.notifications.views import NotificationViewSet
from school_1329_server.schedule.views import ScheduleSubjectViewSet, ScheduleLessonViewSet
from school_1329_server.users.views import UsersViewSet

router = SimpleRouter(trailing_slash=False)
router.register('users', UsersViewSet, 'users')
router.register('groups', GroupsViewSet, 'groups')
router.register('events', EventsViewSet, 'events')
router.register('event_comments', EventCommentsViewSet, 'event_comments')
router.register('schedule_lessons', ScheduleLessonViewSet, 'schedule_lessons')
router.register('schedule_subjects', ScheduleSubjectViewSet, 'schedule_subjects')
router.register('notifications', NotificationViewSet, 'notifications')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
