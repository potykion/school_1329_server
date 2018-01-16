from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from school_1329_server.users.models import RegistrationCode, User, UserLevel
from school_1329_server.users.utils import generate_registration_code


class RegistrationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationCode
        fields = ('expiration_date', 'code', 'level')
        extra_kwargs = {
            'code': {'read_only': True}
        }

    def validate_expiration_date(self, value):
        if value > timezone.now():
            return value
        else:
            raise ValidationError('Expiration date should be greater than {}.'.format(timezone.now()))

    def validate(self, data):
        return {**data, 'code': generate_registration_code()}


class ValidateRegistrationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationCode
        fields = ('code', 'level')

    def validate(self, data):
        """
        Check password exists, and password expiration date greater that now date.
        :param data: Dict of value and level keys.
        :return: Validation result.
        """
        try:
            password = RegistrationCode.objects.filter(**data).get()
        except RegistrationCode.DoesNotExist:
            raise ValidationError({'code': 'No such password.'})
        else:
            if password.expiration_date > timezone.now():
                return {'valid': True}
            else:
                raise ValidationError({'expiration_date': 'Password date is expired.'})


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'level')

    def validate_level(self, value):
        """
        Validate level is teacher or student.
        :param value: Level value.
        :return: Validated level.
        """
        if value in [UserLevel.teacher, UserLevel.student]:
            return value
        else:
            raise ValidationError('Invalid level.')
