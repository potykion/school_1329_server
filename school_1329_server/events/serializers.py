from rest_framework import serializers

from school_1329_server.events.models import Event


class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = (
            'id', 'title', 'place', 'description',
            'participation_groups', 'created_by',
            'start_date', 'end_date'
        )
        extra_kwargs = {
            'created_by': {
                'required': False
            }
        }
