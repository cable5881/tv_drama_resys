from rest_framework import serializers

from meiju.models.drama_type import DramaType


class DramaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DramaType
        fields = (
            'type',
        )
