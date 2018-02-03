from rest_framework import serializers

from school_1329_server.schedule.models import ScheduleSubject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleSubject
        fields = ('title', 'id')
