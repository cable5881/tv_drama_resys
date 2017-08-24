from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView

from accounts.models import MyUser


class SpaceView(LoginRequiredMixin, TemplateView):
    template_name = 'space/space.html'

    def get_context_data(self, **kwargs):
        request = self.request

        if 'user_id' in self.kwargs:
            user_id = int(self.kwargs['user_id'])
        else:
            user_id = request.user.id

        if user_id == request.user.id:
            check_user = request.user
        else:
            check_user = MyUser.objects.get(pk=user_id)
            kwargs['followed'] = True if request.user.followings.filter(following=check_user).exists() else False

        kwargs['check_user'] = check_user
        kwargs['hot_reviews'] = check_user.reviews.exclude(Q(title='') | Q(title=None))[0:2]
        kwargs['watched_reviews'] = check_user.reviews.filter(is_watched=True)
        kwargs['unwatched_reviews'] = check_user.reviews.filter(is_watched=False)
        kwargs['recent_review_likes'] = check_user.review_likes.order_by('like_time')[0:2]
        kwargs['sexes'] = MyUser.SEX_CHOICES
        return super(SpaceView, self).get_context_data(**kwargs)

# If the user isn’t logged in, redirect to settings.LOGIN_URL,
# passing the current absolute path in the query string.
# @login_required
# def to_space(request):
# if not request.user.is_authenticated:
#     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
# return render(request, 'space/space.html')


# @permission_required('polls.can_vote', raise_exception=True)
# def my_view(request):
#     ...
