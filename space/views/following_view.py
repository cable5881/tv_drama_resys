from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from accounts.entities.follower import Follower
from accounts.entities.following import Following
from accounts.models import MyUser


def to_following(request):
    return render(request, 'space/following.html')


class FollowingView(LoginRequiredMixin, ListView):
    template_name = 'space/following.html'
    paginate_by = settings.OBJECTS_NUM_PER_PAGE

    def get_queryset(self):
        request = self.request
        user_id = int(self.kwargs['user_id'])
        if request.user.is_authenticated and user_id == request.user.id:
            check_user = request.user
        else:
            check_user = MyUser.objects.get(pk=user_id)

        self.queryset = Following.objects.filter(user=check_user)
        self.kwargs['check_user'] = check_user
        return super(FollowingView, self).get_queryset()

    def get_context_data(self, **kwargs):
        return super(FollowingView, self).get_context_data(check_user=self.kwargs['check_user'])


class AddFollowingView(View):
    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            following_id = int(request.POST['following_id'])
            following_qset = MyUser.objects.filter(pk=following_id)
            if following_qset.exists():
                following_user = following_qset.get()
                following = Following()
                following.user = self.request.user
                following.following = following_user
                following.save()

                follower = Follower()
                follower.user = following_user
                follower.follower = self.request.user
                follower.save()

                data = {
                    'msg': '关注成功！',
                }
                return JsonResponse(data)

        raise Http404("Drama does not exist")


class DeleteFollowingView(View):
    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            following_id = int(request.POST['fid'])
            user_id = request.user.id
            Following.objects.filter(following_id=following_id, user_id=user_id).delete()
            Follower.objects.filter(follower_id=user_id, user_id=following_id).delete()

            data = {
                'msg': '取消关注成功！',
            }
            return JsonResponse(data)

        raise Http404("Drama does not exist")
