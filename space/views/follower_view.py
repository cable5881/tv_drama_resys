from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from accounts.entities.follower import Follower
from accounts.models import MyUser


class FollowerView(LoginRequiredMixin, ListView):
    template_name = 'space/follower.html'
    paginate_by = settings.OBJECTS_NUM_PER_PAGE

    def get_queryset(self):
        request = self.request
        user_id = int(self.kwargs['user_id'])
        if request.user.is_authenticated and user_id == request.user.id:
            check_user = request.user
        else:
            check_user = MyUser.objects.get(pk=user_id)

        self.queryset = Follower.objects.filter(user=check_user)
        self.kwargs['check_user'] = check_user
        return super(FollowerView, self).get_queryset()

    def render_to_response(self, context, **response_kwargs):
        followings = self.request.user.followings.all()
        following_arr = []
        for f in followings:
            following_arr.append(f.following_id)
        context['followings'] = following_arr

        context['check_user'] = self.kwargs['check_user']
        
        return super(FollowerView, self).render_to_response(context, **response_kwargs)


