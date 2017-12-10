from django.urls import path

from school_1329_server.users import views

urlpatterns = [
    path('generate_password', views.CreateTemporaryPasswordAPIView.as_view()),
    path('validate_password', views.ValidateTemporaryPasswordAPIView.as_view()),
    path('register', views.CreateUserAPIView.as_view()),
]
