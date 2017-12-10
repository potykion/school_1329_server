from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from school_1329_server.users.models import User, UserLevel


class TeacherAuthorization(BaseAuthentication):
    """
    Authorize teacher by username.
    """

    def authenticate(self, request):

        username = request.data.get('username')

        try:
            teacher = User.objects.get(username=username, level=UserLevel.teacher)
        except User.DoesNotExist:
            raise AuthenticationFailed('No such teacher.')

        return teacher, username
