from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from school_1329_server.groups.models import Group
from school_1329_server.groups.serializers import GroupSerializer


class GroupsViewSet(ModelViewSet):
    """
    Group related methods.

    Already included methods:
    - list (GET: /api/groups) - list all of the Groups
    - create (POST: /api/groups) - create Group with title
    - destroy (DELETE: /api/groups/{pk}) - delete Group with pk
    - put (PUT: /api/groups/{pk}) - update Group with pk
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @detail_route(methods=['post'])
    def add_user(self, request: Request, pk=None):
        """
        Add user to group with {pk}.
        :return: Response contains success flag or errors.
        """
        group = self.get_object()
        group.users.add(request.user)
        group.save()

        return Response({'success': True})
