from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from school_1329_server.common.mixins import SuccessDestroyMixin
from school_1329_server.events.models import Event, EventComment
from school_1329_server.events.serializers import EventSerializer, EventCommentSerializer


class EventsViewSet(SuccessDestroyMixin, ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)


class EventCommentsViewSet(SuccessDestroyMixin, ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
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
