
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from school_1329_server.users.auth import TeacherAuthorization
from school_1329_server.users.serializers import TemporaryPasswordSerializer, ValidateTemporaryPasswordSerializer, \
    UserSerializer



class CreateTemporaryPasswordAPIView(CreateAPIView):
    """
    Generate temporary password with given date and level.
    """
    serializer_class = TemporaryPasswordSerializer


class ValidateTemporaryPasswordAPIView(APIView):
    """
    Validate temporary password by given value and level.
    """

    def post(self, request, *args, **kwargs):
        serializer = ValidateTemporaryPasswordSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)
        else:
            return Response({'valid': False}, status=400)


class CreateUserAPIView(CreateAPIView):
    """
    Validate input password value, create user with input username.
    """
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = ValidateTemporaryPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super(CreateUserAPIView, self).post(request, *args, **kwargs)


class CreateTeacherAdminPasswordAPIView(APIView):
    """
    Get teacher by username, set and generate password for admin page.
    """
    authentication_classes = (TeacherAuthorization,)

    def post(self, request, *args, **kwargs):
        return Response({'password_value': request.user.generate_password()}, 200)




