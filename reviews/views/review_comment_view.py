from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView
from rest_framework import generics
from rest_framework import permissions

from reviews.forms.review_comment_form import ReviewCommentForm
from reviews.models.review import Review
from reviews.models.review_comment import ReviewComment
from reviews.permissions.is_owner_or_read_only import IsOwnerOrReadOnly
from reviews.serializers.review_comment_serializer import ReviewCommentSerializer
from tv_drama_resys import settings


class ReviewCommentView(ListView):
    model = ReviewComment
    template_name = 'drama/review_detail.html'
    paginate_by = settings.OBJECTS_NUM_PER_PAGE

    def get_queryset(self):
        self.queryset = ReviewComment.objects.filter(review=self.kwargs['pk'])
        return super(ReviewCommentView, self).get_queryset()

    def render_to_response(self, context, **response_kwargs):
        review = Review.objects.get(id=self.kwargs['pk'])
        context['review'] = review
        review_like = review.review_likes.filter(user=self.request.user)
        if review_like.exists():
            context['review_like'] = review_like.get()

        return super(ReviewCommentView, self).render_to_response(context, **response_kwargs)


class ReviewCommantAjaxableResponseMixin(object):
    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            raise Http404("Poll does not exist")

    def form_valid(self, form):
        review_comment = form.save(False)
        review_comment.user = self.request.user
        form.save(commit=True)

        if self.request.is_ajax():
            data = {
                'msg': '添加成功！',
            }
            return JsonResponse(data)
        else:
            raise Http404("Poll does not exist")


class AddReviewCommentView(LoginRequiredMixin, ReviewCommantAjaxableResponseMixin, BaseFormView):
    form_class = ReviewCommentForm



class ReviewCommentList(generics.ListCreateAPIView):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer

    # that allows us to modify how the instance save is managed,
    # and handle any information that is implicit in the incoming request or requested URL.
    # 在保存之前把登录的user字段插入将要被保存的Review中
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReviewCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer

    # 加上IsOwnerOrReadOnly是为了自己创建的ReviewComment才能被自己删除而不被其他User删除
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
