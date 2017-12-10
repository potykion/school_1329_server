from rest_framework.generics import CreateAPIView

from school_1329_server.users.serializers import TemporaryPasswordSerializer


class CreateStudentTemporaryPasswordAPIView(CreateAPIView):
    """
    Generate temporary password with given date and level.
    """
    serializer_class = TemporaryPasswordSerializer
