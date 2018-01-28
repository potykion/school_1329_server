from rest_framework import serializers

from school_1329_server.events.models import Event, EventComment


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


class EventCommentSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = EventComment
        fields = (
            'id', 'text', 'created_by', 'created', 'event'
        )
        extra_kwargs = {
            'created_by': {'required': False},
            'event': {'write_only': True}
        }
