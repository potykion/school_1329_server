import pytest
from django.http import HttpResponse, HttpResponseRedirect
from django.test import Client
from django.urls import reverse

from school_1329_server.users.models import User
from tests.users.setup import UsersFixtures


class TestCommonViews(UsersFixtures):
    def test_index_view(self, client: Client):
        """
        Given index view url,
        When go to index view url,
        Then url is root,
        And response contains welcome info.
        """
        url = reverse('index')

        response: HttpResponse = client.get(url)

        assert url == '/'
        assert 'Здравствуйте' in response.content.decode('utf-8')

    def test_login_view_get(self, client: Client):
        """
        Given login url,
        When go to login url,
        Then response contains login form.
        """
        url = reverse('login')

        response: HttpResponse = client.get(url)

        assert 'form' in response.content.decode('utf-8')

    def test_login_view_post_with_valid_login(self, client: Client, user: User):
        """
        Given user,
        And login url,
        When send post to login url with user data,
        Then response redirects to admin page,
        And user is authorized.
        """
        url = reverse('login')

        response: HttpResponseRedirect = client.post(url, {
            'username': user.username,
            'password': "verysecretpassword"
        })

        assert response.url == reverse('admin')
        assert '_auth_user_id' in client.session

    def test_admin_view_without_login(self, client: Client, user: User):
        """
        Given admin url,
        And user,
        When go to admin url,
        And user is not authorized,
        Then response redirects to login view.
        """
        url = reverse('admin')

        response: HttpResponseRedirect = client.get(url)

        assert response.url == reverse('login') + '?next=/admin'
