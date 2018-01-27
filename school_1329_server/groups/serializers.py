from rest_framework import serializers

from school_1329_server.groups.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title')
