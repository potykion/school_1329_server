from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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


class ValidateTemporaryPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryPassword
        fields = ('value', 'level')

    def validate(self, data):
        """
        Check password exists, and password expiration date greater that now date.
        :param data: Dict of value and level keys.
        :return: Validation result.
        """
        try:
            password = TemporaryPassword.objects.filter(**data).get()
        except TemporaryPassword.DoesNotExist:
            raise ValidationError({'password': 'No such password.'})
        else:
            if password.expiration_date > timezone.now():
                return {'valid': True}
            else:
                raise ValidationError({'expiration_date': 'Password date is expired.'})
