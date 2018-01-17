from rest_framework.authtoken.models import Token
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from school_1329_server.users import serializers
from school_1329_server.users.models import RegistrationCode


class UsersViewSet(GenericViewSet):
    """
    User related actions (registration code generation, user registration, etc.).
    """

    @list_route(methods=['post'])
    def create_code(self, request):
        """
        Validate date and level, create registration code.
        :param request: Request.
        :return: Generated registration code.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code: RegistrationCode = serializer.save()

        return Response({'code': code.code}, status=200)

    @list_route(methods=['post'])
    def check_code(self, request):
        """
        Validate registration code data (level, code).
        :param request: Request.
        :return: True if code data is correct, false otherwise.
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            return Response({'correct': True}, status=200)
        else:
            return Response({'correct': False}, status=400)

    @list_route(methods=['post'])
    def register(self, request):
        """
        Validate register code data (code, level), create new user with user data (level, password, username).
        :param request: Request.
        :return: User token.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = Token.objects.create(user=user)

        return Response({'token': token.key}, status=200)

    def get_serializer_class(self):
        """
        Pick serializer class depends on action.
        :return: Serializer class.
        """
        if self.action == 'create_code':
            return serializers.RegistrationCodeSerializer
        elif self.action == 'check_code':
            return serializers.ValidateRegistrationCodeSerializer
        elif self.action == 'register':
            return serializers.UserSerializer
