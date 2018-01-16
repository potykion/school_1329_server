from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView

from school_1329_server.users.forms import RegistrationCodeForm
from school_1329_server.users.models import RegistrationCode


class CreateRegistrationCodeView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'users/create_code.html'
    form_class = RegistrationCodeForm
    success_url = reverse_lazy('list_codes')
    success_message = 'Пароль создан успешно.'


class ListRegistrationCodesView(LoginRequiredMixin, ListView):
    template_name = 'users/list_codes.html'
    context_object_name = 'codes'
    queryset = RegistrationCode.objects.filter(
        expiration_date__gt=timezone.now()
    ).order_by(
        '-date_created'
    )
