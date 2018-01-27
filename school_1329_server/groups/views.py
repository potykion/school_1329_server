from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from school_1329_server.common.mixins import SuccessDestroyMixin
from school_1329_server.events.serializers import EventSerializer
from school_1329_server.groups.models import Group
from school_1329_server.groups.serializers import GroupSerializer
from school_1329_server.users.serializers import UserSerializer


class GroupsViewSet(SuccessDestroyMixin, ModelViewSet):
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

    @detail_route()
    def events(self, request, pk=None):
        """
        List group events.
        :return: Group events.
        """
        group = self.get_object()
        events = group.event_set.all()
        serializer: EventSerializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'users':
            return UserSerializer
        elif self.action == 'events':
            return EventSerializer
        else:
            return GroupSerializer
