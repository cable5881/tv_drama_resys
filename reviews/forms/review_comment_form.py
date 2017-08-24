from django.forms import ModelForm

from reviews.models.review_comment import ReviewComment


class ReviewCommentForm(ModelForm):
    class Meta:
        model = ReviewComment
        fields = ['content', 'review']


