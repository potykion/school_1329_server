from itertools import groupby
from operator import itemgetter

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from school_1329_server.common.mixins import SuccessDestroyMixin
from school_1329_server.groups.models import Group
from school_1329_server.schedule.models import ScheduleSubject, ScheduleLesson, Weekdays
from school_1329_server.schedule.serializers import ScheduleSubjectSerializer, UserScheduleLessonsSerializer, \
    ScheduleLessonSerializer


class ScheduleSubjectViewSet(SuccessDestroyMixin, ModelViewSet):
    serializer_class = ScheduleSubjectSerializer
    queryset = ScheduleSubject.objects.all()


class ScheduleLessonViewSet(SuccessDestroyMixin, ModelViewSet):
    queryset = ScheduleLesson.objects.all()

    @list_route()
    def user_schedule(self, request, *args, **kwargs):
        user_groups = Group.objects.filter(users__in=[request.user])
        user_lessons = ScheduleLesson.objects.filter(groups__in=user_groups)

        serializer = self.get_serializer(user_lessons, many=True)
        serialized_lessons = serializer.data

        schedule = self.build_schedule(serialized_lessons)
        return Response(schedule)

    def build_schedule(self, serialized_lessons):
        weekday_lessons = groupby(
            serialized_lessons,
            key=lambda item: item.pop('weekday')
        )

        schedule = dict.fromkeys(map(itemgetter(0), Weekdays.choices), [])
        for weekday, items in weekday_lessons:
            schedule[weekday] = list(items)

        return schedule

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

    def perform_update(self, serializer):
        serializer.save(teacher=self.request.user)

    def get_serializer_class(self):
        if self.action == 'user_schedule':
            return UserScheduleLessonsSerializer
        else:
            return ScheduleLessonSerializer
