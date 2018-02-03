from rest_framework.viewsets import ModelViewSet

from school_1329_server.common.mixins import SuccessDestroyMixin
from school_1329_server.schedule.models import ScheduleSubject
from school_1329_server.schedule.serializers import SubjectSerializer


class SubjectViewSet(SuccessDestroyMixin, ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = ScheduleSubject.objects.all()
