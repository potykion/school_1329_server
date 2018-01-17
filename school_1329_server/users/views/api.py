from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from school_1329_server.users import serializers


class CreateRegistrationCodeAPIView(CreateAPIView):
    """
    Generate temporary password with given date and level.
    """
    serializer_class = serializers.RegistrationCodeSerializer

    def post(self, request, *args, **kwargs):
        response = super(CreateRegistrationCodeAPIView, self).post(request, *args, **kwargs)
        return Response({'code': response.data['code']}, status=200)


class CheckRegistrationCodeAPIView(APIView):
    """
    Validate temporary password by given value and level.
    """

    def post(self, request, *args, **kwargs):
        serializer = serializers.ValidateRegistrationCodeSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'correct': True}, status=200)
        else:
            return Response({'correct': False}, status=400)


class RegisterUserAPIView(CreateAPIView):
    """
    Validate input password value, create user with input username.
    """
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.ValidateRegistrationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super(RegisterUserAPIView, self).post(request, *args, **kwargs)
