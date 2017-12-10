from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from school_1329_server.users.serializers import TemporaryPasswordSerializer, ValidateTemporaryPasswordSerializer


class CreateTemporaryPasswordAPIView(CreateAPIView):
    """
    Generate temporary password with given date and level.
    """
    serializer_class = TemporaryPasswordSerializer


class ValidateTemporaryPasswordAPIView(APIView):
    """
    Validate temporary password with given value and level.
    """

    def post(self, request, *args, **kwargs):
        serializer = ValidateTemporaryPasswordSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)
        else:
            return Response({'valid': False}, status=400)
