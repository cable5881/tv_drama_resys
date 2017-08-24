from meiju.models.drama import Drama
from rest_framework import serializers

from meiju.models.drama_type import DramaType


class DramaSerializer(serializers.ModelSerializer):
    types = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='type'
    )
    # type = serializers.ReadOnlyField(source='types.type')

    class Meta:
        model = Drama
        fields = (
            'id', 'title_cn', 'image', 'title_en', 'year', 'episodes', 'types', 'summary',
            'avg_rating', 'douban_url', 'seasons_count', 'current_season', 'alternate_name',
        )
