from django.urls import path

from school_1329_server.users.views import CreateStudentTemporaryPasswordAPIView

urlpatterns = [
    path('generate_password', CreateStudentTemporaryPasswordAPIView.as_view())
]
