from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from school_1329_server.groups.models import Group
from school_1329_server.groups.serializers import GroupSerializer
from school_1329_server.users.serializers import UserSerializer


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

    @detail_route(methods=['post'])
    def add_user(self, request: Request, pk=None):
        """
        Add user to group with {pk}.
        :return: Success flag.
        """
        group = self.get_object()
        group.users.add(request.user)
        group.save()

        return Response({'success': True})

    def destroy(self, request, *args, **kwargs):
        """
        Delete group with {pk}.
        :return: Success flag.
        """
        response = super(GroupsViewSet, self).destroy(request, *args, **kwargs)
        return Response({'success': True})

    @detail_route(methods=['post', 'delete'])
    def remove_user(self, request: Request, pk=None):
        """
        Remove token-user from group with {pk}.
        :return: Success flag.
        """
        group = self.get_object()
        group.users.remove(request.user)
        group.save()

        return Response({'success': True})

    @list_route()
    def user_groups(self, request: Request):
        """
        List token-user groups.
        :return: User groups
        """
        groups = request.user.group_set.all()
        serializer: GroupSerializer = self.get_serializer(groups, many=True)
        return Response(serializer.data)

    @detail_route()
    def users(self, request, pk=None):
        """
        List group users.
        :return: Group users.
        """
        group = self.get_object()
        users = group.users.all()
        serializer: UserSerializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'users':
            return UserSerializer
        else:
            return GroupSerializer
