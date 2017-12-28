from datetime import timedelta

from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import Client
from django.urls import reverse
from django.utils import timezone

from school_1329_server.common.utils import response_content_to_str
from school_1329_server.users.models import TemporaryPassword
from tests.users.setup import UsersFixtures


class TestUsersAdminViews(UsersFixtures):
    def test_generate_password_view_render(self, client: Client, user):
        """
        Given generate password url,
        And user,
        When authorize user,
        And go to given url
        Then response contains password generation form.
        """
        url = reverse('generate_password')

        client.post(reverse('login'), {
            'username': user.username,
            'password': "verysecretpassword"
        })
        response: TemplateResponse = client.get(url)

        rendered = response.content.decode('utf-8')
        assert 'form' in rendered
        assert 'expiration_date' in rendered
        assert 'password_value' in rendered

    def test_generate_password_view_POST(self, client: Client, user):
        """
        Given generate password url,
        And user,
        And password,
        And date
        When send POST to given url with password and date,
        Then password is created,
        And response redirects to password list.
        """
        url = reverse('generate_password')

        password = 'verysecretpassword'
        date = timezone.now() + timedelta(days=2)

        client.post(reverse('login'), {
            'username': user.username,
            'password': "verysecretpassword"
        })
        response: HttpResponseRedirect = client.post(url, {
            'password_value': password,
            'expiration_date': date.date()
        })

        assert TemporaryPassword.objects.filter(password_value=password, expiration_date__date=date).exists()
        assert response.url == reverse('password_list')

    def test_generate_password_with_expired_expiration_date(self, client: Client, user):
        """
        Given generate password url,
        And user,
        And password,
        And expired date
        When send POST to given url with password and date,
        Then response contains date error,
        And no passwords were created.
        """
        url = reverse('generate_password')

        password = 'verysecretpassword1'
        date = timezone.now() - timedelta(days=2)

        client.post(reverse('login'), {
            'username': user.username,
            'password': "verysecretpassword"
        })
        response: HttpResponseRedirect = client.post(url, {
            'password_value': password,
            'expiration_date': date.date()
        })

        assert 'Дата или пароль указаны неверно' in response_content_to_str(response)
        assert not TemporaryPassword.objects.filter(password_value=password).exists()
