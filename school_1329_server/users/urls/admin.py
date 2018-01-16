from django.urls import path

from school_1329_server.users.views import admin as views

urlpatterns = [
    path('create_code', views.CreateRegistrationCodeView.as_view(), name='create_code'),
    path('list_codes', views.ListRegistrationCodesView.as_view(), name='list_codes')
]
