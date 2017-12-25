from django import forms

from school_1329_server.users.models import TemporaryPassword


class GeneratePasswordForm(forms.ModelForm):
    class Meta:
        model = TemporaryPassword
        fields = ('expiration_date', 'password_value')
