from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from school_1329_server.users.forms import GeneratePasswordForm


class GeneratePasswordView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'users/generate_password.html'
    form_class = GeneratePasswordForm
    success_url = reverse_lazy('generate_password')
    success_message = 'Пароль создан успешно.'
