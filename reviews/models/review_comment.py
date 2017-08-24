from django.conf import settings
from django.db import models

from reviews.models.review import Review


class ReviewComment(models.Model):
    review = models.ForeignKey(Review, related_name='review_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=255)
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.nickname + ':' + self.review.title

    class Meta:
        db_table = 'reviews_comment'
