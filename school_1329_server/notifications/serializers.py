from rest_framework import serializers

from school_1329_server.notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Notification
        fields = (
            'id', 'text', 'send_once', 'groups', 'frequency', 'created_by'
        )
        extra_kwargs = {
            'created_by': {'write_only': True, 'required': False},
        }
