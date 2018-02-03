from rest_framework import serializers

from school_1329_server.schedule.models import ScheduleSubject, ScheduleLesson


class ScheduleSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleSubject
        fields = ('title', 'id')


class ScheduleLessonSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()

    class Meta:
        model = ScheduleLesson
        fields = (
            'id', 'start_time', 'weekday',
            'subject', 'teacher', 'groups'
        )
        extra_kwargs = {
            'teacher': {'required': False}
        }


class UserScheduleLessonsSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    teacher = serializers.StringRelatedField()

    class Meta:
        model = ScheduleLesson
        fields = (
            'id', 'start_time', 'weekday',
            'subject', 'teacher', 'groups'
        )
        extra_kwargs = {
            'groups': {'write_only': True},
            'teacher': {'required': False}
        }
