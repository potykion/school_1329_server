from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView

from school_1329_server.users.forms import GeneratePasswordForm
from school_1329_server.users.models import TemporaryPassword


class GeneratePasswordView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'users/generate_password.html'
    form_class = GeneratePasswordForm
    success_url = reverse_lazy('password_list')
    success_message = 'Пароль создан успешно.'


class ListGeneratedPasswords(LoginRequiredMixin, ListView):
    template_name = 'users/password_list.html'
    context_object_name = 'passwords'
    queryset = TemporaryPassword.objects.filter(expiration_date__gt=timezone.now()).order_by('-date_created')
