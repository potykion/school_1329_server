from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request

from school_1329_server.users.models import User


class LoginAuthentication(BaseAuthentication):
    """
    Authorize user by {username} and {password} from request body.
    """

    def authenticate(self, request: Request):
        username, password = request.data['username'], request.data['password']

        try:
            user = User.objects.filter(username=username, password=password).get()
        except User.DoesNotExist:
            return None
        else:
            return user, None
