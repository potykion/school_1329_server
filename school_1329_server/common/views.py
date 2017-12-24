from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index_view(request: HttpRequest) -> HttpResponse:
    """
    Renders index page.
    :param request: HttpRequest.
    :return: HttpResponse with rendered index page.
    """
    return render(request, "common/index.html")


class AdminLoginView(LoginView):
    """
    On GET renders login form, on POST redirects to success url or shows error message.
    """
    template_name = "common/login.html"


@login_required()
def admin_view(request: HttpRequest) -> HttpResponse:
    """
    Admin page.
    :param request: HttpRequest.
    :return: Admin page.
    """
    return HttpResponse("Admin page.")
