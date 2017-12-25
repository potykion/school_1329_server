from django.urls import path

from school_1329_server.users.views import admin as views

urlpatterns = [
    path('generate_password', views.GeneratePasswordView.as_view(), name='generate_password')

]
