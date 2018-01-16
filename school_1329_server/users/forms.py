from django import forms
from django.utils import timezone

from school_1329_server.users.models import RegistrationCode


class RegistrationCodeForm(forms.ModelForm):
    class Meta:
        model = RegistrationCode
        fields = ('expiration_date', "code")

    def clean_expiration_date(self):
        """
        Validate expiration date by comparing it with today's date.
        :param date: Expiration date.
        :return: Expiration date.
        :raise: ValidationError if date is less than today's date.
        """
        date = self.cleaned_data['expiration_date']
        if timezone.now() > date:
            raise forms.ValidationError('Date should be greater than today.')

        return date
