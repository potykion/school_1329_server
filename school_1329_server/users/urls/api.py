from django.urls import path

from school_1329_server.users.views import api as views

urlpatterns = [
    path('create_code', views.CreateRegistrationCodeAPIView.as_view()),
    path('check_code', views.CheckRegistrationCodeAPIView.as_view()),
    path('register', views.RegisterUserAPIView.as_view()),
]
