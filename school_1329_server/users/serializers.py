from rest_framework import serializers

from school_1329_server.users.models import TemporaryPassword
from school_1329_server.users.utils import generate_password


class TemporaryPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryPassword
        fields = ('expiration_date', 'value', 'level')
        extra_kwargs = {
            'value': {'read_only': True}
        }

    def validate(self, data):
        return {
            **data,
            'value': generate_password()
        }
