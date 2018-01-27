from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from school_1329_server.common.mixins import SuccessDestroyMixin
from school_1329_server.events.models import Event
from school_1329_server.events.serializers import EventSerializer


class EventsViewSet(SuccessDestroyMixin, ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)
