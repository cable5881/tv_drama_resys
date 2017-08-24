from django.contrib import admin
from reviews.models.review import Review
from reviews.models.review_likes import ReviewLikes
from reviews.models.review_comment import ReviewComment

admin.site.register(Review)
admin.site.register(ReviewLikes)
admin.site.register(ReviewComment)

