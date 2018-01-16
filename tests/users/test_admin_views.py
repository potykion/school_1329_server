from datetime import timedelta

from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import Client
from django.urls import reverse
from django.utils import timezone

from school_1329_server.common.utils import response_content_to_str
from school_1329_server.users.models import RegistrationCode
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
        url = reverse('create_code')

        client.post(reverse('login'), {
            'username': user.username,
            'password': "verysecretpassword"
        })
        response: TemplateResponse = client.get(url)

        rendered = response.content.decode('utf-8')
        assert 'form' in rendered
        assert 'expiration_date' in rendered
        assert 'code' in rendered

    def test_generate_password_view_POST(self, client: Client, user):
        """
        Given generate password url,
        And user,
        And registration code,
        And date
        When send POST to given url with password and date,
        Then password is created,
        And response redirects to password list.
        """
        url = reverse('create_code')

        code = 'verysecretpassword'
        date = timezone.now() + timedelta(days=2)

        client.post(reverse('login'), {
            'username': user.username,
            'password': "verysecretpassword"
        })
        response: HttpResponseRedirect = client.post(url, {
            'code': code,
            'expiration_date': date.date()
        })

        assert RegistrationCode.objects.filter(
            code=code,
            expiration_date__date=date
        ).exists()
        assert response.url == reverse('list_codes')

    def test_generate_password_with_expired_expiration_date(self, client: Client, user):
        """
        Given generate password url,
        And user,
        And registration code,
        And expired date
        When send POST to given url with password and date,
        Then response contains date error,
        And no passwords were created.
        """
        url = reverse('create_code')

        code = 'verysecretpassword1'
        date = timezone.now() - timedelta(days=2)

        client.post(reverse('login'), {
            'username': user.username,
            'password': "verysecretpassword"
        })
        response: HttpResponseRedirect = client.post(url, {
            'code': code,
            'expiration_date': date.date()
        })

        assert 'Дата или пароль указаны неверно' in response_content_to_str(response)
        assert not RegistrationCode.objects.filter(
            code=code
        ).exists()
