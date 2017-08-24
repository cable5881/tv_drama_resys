from django.conf import settings
from django.db import models

from reviews.models.review import Review


class ReviewLikes(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_likes')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='review_likes',
    )
    like_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.nickname + ':' + self.review.title

    class Meta:
        db_table = 'reviews_likes'
