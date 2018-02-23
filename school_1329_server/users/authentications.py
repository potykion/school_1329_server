from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request

from school_1329_server.users.models import User


class LoginAuthentication(BaseAuthentication):
    """
    Authorize user by {username} and {password} from request body.
    """

    def authenticate(self, request: Request):
        username, password = request.data['username'], request.data['password']
        fcm_token = request.data.get('fcm_token')

        try:
            user = User.objects.filter(username=username, password=password).get()
        except User.DoesNotExist:
            return None
        else:
            if fcm_token:
                user.fcm_token = fcm_token
                user.save()

            return user, None
