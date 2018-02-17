from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from school_1329_server.common.mixins import SuccessDestroyMixin
from school_1329_server.events.models import Event, EventComment
from school_1329_server.events.serializers import EventSerializer, EventCommentSerializer
from school_1329_server.groups.models import Group


class EventsViewSet(SuccessDestroyMixin, ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

    @list_route()
    def user_entered_events(self, request, *args, **kwargs):
        """
        List events where user participates.
        :return: User-participated events.
        """
        user_groups = Group.objects.filter(users__in=[request.user])
        user_events = Event.objects.filter(participation_groups__in=user_groups)
        serializer: EventSerializer = self.get_serializer(user_events, many=True)
        return Response(serializer.data)

    @list_route()
    def user_created_events(self, request, *args, **kwargs):
        """
        List events which created by user.
        :return: User-created events.
        """
        user_events = Event.objects.filter(created_by=request.user)
        serializer: EventSerializer = self.get_serializer(user_events, many=True)
        return Response(serializer.data)


class EventCommentsViewSet(SuccessDestroyMixin, ModelViewSet):
    serializer_class = EventCommentSerializer

    def get_queryset(self):
        """
        Filter event comments by {event} id if it is present.
        :return: Event comments.
        """
        event_id = self.request.data.get('event') or \
                   self.request.query_params.get('event')

        if event_id:
            return EventComment.objects.filter(event=event_id)
        else:
            return EventComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
