from rest_framework import serializers

from accounts.models import MyUser
from reviews.models.review import Review
from reviews.serializers.review_serializer import ReviewSerializer


class UserSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = MyUser
        exclude = ('id', 'password', 'last_login', 'is_active', 'is_admin',)
