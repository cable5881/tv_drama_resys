from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.http import JsonResponse
from django.views import View
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from rest_framework import permissions
from rest_framework import viewsets

from meiju.models.drama import Drama
from reviews.forms.review_form import ReviewForm, UnwatchedReviewForm
from reviews.models.review import Review
from reviews.permissions.is_owner_or_read_only import IsOwnerOrReadOnly
from reviews.serializers.review_serializer import ReviewSerializer
from tv_drama_resys import settings


class ReviewAjaxableResponseMixin(object):
    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            raise Http404("Poll does not exist")

    def form_valid(self, form):
        review = form.save(False)

        if self.request.POST['pk']:
            review.id = self.request.POST['pk']
            review.is_watched = True
            fields = ['title', 'content', 'rating', 'is_watched']
            review.save(force_update=True, update_fields=fields)
        else:
            review.user = self.request.user
            review.save(True)

        if self.request.is_ajax():
            data = {
                'msg': '保存成功！',
            }
            return JsonResponse(data)
        else:
            raise Http404("Poll does not exist")


class AddReviewView(LoginRequiredMixin, ReviewAjaxableResponseMixin, FormView):
    form_class = ReviewForm
    template_name = 'drama/drama_detail.html'


class AddUnwatchedReviewView(LoginRequiredMixin, FormMixin, View):
    form_class = UnwatchedReviewForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            review = form.save(False)
            review.user = self.request.user
            review.is_watched = False
            review.save(True)

            if self.request.is_ajax():
                data = {
                    'msg': '想看成功！',
                }
                return JsonResponse(data)
            else:
                raise Http404("Drama does not exist")
        else:
            if self.request.is_ajax():
                return JsonResponse(form.errors, status=400)
            else:
                raise Http404("Drama does not exist")


class DeleteReviewView(LoginRequiredMixin, SingleObjectMixin, View):
    model = Review

    def post(self, request, *args, **kwargs):
        self.kwargs['pk'] = request.POST['pk']
        self.kwargs['user'] = request.user
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        review.delete()

        if self.request.is_ajax():
            data = {
                'msg': '删除剧评成功！',
            }
            return JsonResponse(data)
        else:
            raise Http404("review_likes cancelling failed!")


class ReviewListView(ListView):
    template_name = 'drama/review_list.html'
    paginate_by = settings.OBJECTS_NUM_PER_PAGE

    def get_queryset(self):
        self.queryset = Review.objects.filter(drama=self.kwargs['pk']).exclude(Q(title=None) | Q(title=''))
        return super(ReviewListView, self).get_queryset()

    def render_to_response(self, context, **response_kwargs):
        context['drama'] = Drama.objects.get(id=self.kwargs['pk'])
        return super(ReviewListView, self).render_to_response(context, **response_kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'reviews': reverse('review-list', request=request, format=format)
#     })

"""
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # that allows us to modify how the instance save is managed,
    # and handle any information that is implicit in the incoming request or requested URL.
    # 在保存之前把登录的user字段插入将要被保存的Review中
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # 加上IsOwnerOrReadOnly是为了自己创建的Review才能被自己删除而不被其他User删除
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class ReviewComments(generics.GenericAPIView):
    queryset = Review.objects.all()

    def get(self, request, *args, **kwargs):
        review = self.get_object()
        return Response(review.reviewcomment_set)
"""
