from django.forms import ModelForm

from reviews.models.review import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rating', 'drama']


class UnwatchedReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['drama']

