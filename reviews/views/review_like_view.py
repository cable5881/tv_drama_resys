from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.http import JsonResponse
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic.detail import SingleObjectMixin

from reviews.models.review_likes import ReviewLikes


class ReviewLikesAjaxableResponseMixin(object):
    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            raise Http404("review_likes adding failed!")

    def form_valid(self, form):
        review_likes = form.save(False)
        review_likes.user = self.request.user
        review_likes.save(True)

        if self.request.is_ajax():
            data = {
                'msg': '保存成功！',
            }
            return JsonResponse(data)
        else:
            raise Http404("review_likes adding failed!")


class AddReviewLikesView(LoginRequiredMixin, ReviewLikesAjaxableResponseMixin, CreateView):
    model = ReviewLikes
    fields = ['review']
    template_name = 'drama/drama_detail.html'


class DeleteReviewLikesView(LoginRequiredMixin, View):
    model = ReviewLikes

    def delete(self, request, *args, **kwargs):
        review_like = self.get_object()
        review_like.delete()

        if self.request.is_ajax():
            data = {
                'msg': '取消喜欢成功！',
            }
            return JsonResponse(data)
        else:
            raise Http404("review_likes cancelling failed!")

    # Add support for browsers which only accept GET and POST for now.
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_object(self):
        try:
            # Get the single item from the filtered queryset
            queryset = ReviewLikes.objects.filter(id=self.request.POST['pk'])
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("ReviewLikes DoesNotExist")
        return obj
