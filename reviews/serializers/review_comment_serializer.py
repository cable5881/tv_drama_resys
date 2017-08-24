from rest_framework import serializers

from reviews.models.review_comment import ReviewComment


class ReviewCommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.email')
    # review_id = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = ReviewComment
        fields = (
            'content', 'comment_time', 'user_id', 'review_id'
        )
