from rest_framework.decorators import list_route
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from school_1329_server.groups.models import Group
from school_1329_server.notifications.models import Notification
from school_1329_server.notifications.serializers import NotificationSerializer


class NotificationViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @list_route()
    def list_sent_notifications(self, request, *args, **kwargs):
        """
        List sent notifications.
        :return: Notifications with sent equal True.
        """
        user_groups = Group.objects.filter(users__in=[self.request.user])
        notifications = self.get_queryset().filter(sent=True, groups__in=user_groups)
        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data)

    @list_route()
    def list_created_notifications(self, request, *args, **kwargs):
        """
        List created by token-user notifications.
        :return: Created by token-user notifications.
        """
        notifications = self.get_queryset().filter(created_by=self.request.user)
        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data)


    def perform_create(self, serializer):
        # todo create notification task with eta = iter.get_next(datetime)
        # https://pypi.python.org/pypi/croniter/
        return serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)
