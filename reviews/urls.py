from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from reviews.views import review_comment_view
from reviews.views import review_like_view
from reviews.views import review_view
from reviews.views.review_view import ReviewViewSet

app_name = 'reviews'

review_list = ReviewViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
review_detail = ReviewViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^dramas/(?P<pk>[0-9]+)/review/$', review_view.ReviewListView.as_view(), name='review_list'),
    url(r'^reviews/add_review/$', review_view.AddReviewView.as_view(), name='add_review'),
    url(r'^reviews/add_review_comment/$', review_comment_view.AddReviewCommentView.as_view(), name='add_review_comment'),
    url(r'^reviews/add_review_likes/$', review_like_view.AddReviewLikesView.as_view(), name='add_review_likes'),
    url(r'^reviews/delete_review/$', review_view.DeleteReviewView.as_view(), name='delete_review'),
    url(r'^reviews/unwatch_review/$', review_view.AddUnwatchedReviewView.as_view(), name='unwatch_review'),
    url(r'^reviews/delete_review_likes/$', review_like_view.DeleteReviewLikesView.as_view(), name='delete_review_likes'),
    url(r'^reviews/(?P<pk>[0-9]+)/$', review_comment_view.ReviewCommentView.as_view(), name='review_detail'),

    # url(r'^reviews/$', review_list, name='review-list'),
    # url(r'^reviews/(?P<pk>[0-9]+)/$', review_detail, name='review-detail'),
    # url(r'^review-comments/$', review_comment_view.ReviewCommentList.as_view(), name='review-comment-list'),
    # url(r'^review-comments/(?P<pk>[0-9]+)/$', review_comment_view.ReviewCommentDetail.as_view(), name='review-comment-detail'),
]
