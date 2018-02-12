from rest_framework import serializers

from school_1329_server.schedule.models import ScheduleSubject, ScheduleLesson
from school_1329_server.schedule.utils import compute_end_time


class ScheduleSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleSubject
        fields = ('title', 'id')


class ScheduleLessonSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()

    class Meta:
        model = ScheduleLesson
        fields = (
            'id', 'start_time', 'end_time', 'weekday', 'place',
            'subject', 'teacher', 'groups'
        )
        extra_kwargs = {
            'teacher': {'required': False},
            'end_time': {'required': False}
        }

    def validate(self, data):
        # set end time if not present
        data.setdefault('end_time', compute_end_time(data['start_time']))
        return data


class UserScheduleLessonsSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    teacher = serializers.StringRelatedField()

    class Meta:
        model = ScheduleLesson
        fields = (
            'id', 'start_time', 'end_time', 'weekday', 'place',
            'subject', 'teacher',
        )
