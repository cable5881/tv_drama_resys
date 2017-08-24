from django.contrib.auth import get_user_model
from rest_framework import serializers

from reviews.models.review import Review
from reviews.models.review_comment import ReviewComment


class ReviewSerializer(serializers.ModelSerializer):
    # 如果不加下面这个的话读取review时的user_id字段是id
    # 加上后该字段变成了email，但是post一个Review时并没有提交该字段
    # 而且这里的需求也是登录的用户才能post
    user_id = serializers.ReadOnlyField(source='user.email')

    review_comments = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='review-comment-detail',
        queryset=ReviewComment.objects.all()
    )

    class Meta:
        model = Review
        fields = (
            'title', 'content', 'rating', 'pubtime', 'user_id', 'review_comments', 'drama'
        )
