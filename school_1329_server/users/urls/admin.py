from django.urls import path

from school_1329_server.users.views import admin as views

urlpatterns = [
    path('generate_password', views.GeneratePasswordView.as_view(), name='generate_password'),
    path('password_list', views.ListGeneratedPasswords.as_view(), name='password_list')
]
