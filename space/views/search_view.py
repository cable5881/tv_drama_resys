from django.conf import settings
from django.db.models import Q
from django.views.generic import ListView

from accounts.models import MyUser


class PeopleSearchView(ListView):
    template_name = 'space/people_search.html'
    paginate_by = settings.OBJECTS_NUM_PER_PAGE

    def get_queryset(self):
        key = self.kwargs['search_text']
        self.queryset = MyUser.objects.filter(
            (Q(nickname__contains=key) | Q(email__contains=key)) &
            Q(is_admin=False)
        ).exclude(id=self.request.user.id).order_by('-date_joined')

        return super(PeopleSearchView, self).get_queryset()

    def render_to_response(self, context, **response_kwargs):
        followings = self.request.user.followings.all()
        following_arr = []
        for f in followings:
            following_arr.append(f.following_id)
        context['followings'] = following_arr

        context['search_text'] = self.kwargs['search_text']

        return super(PeopleSearchView, self).render_to_response(context, **response_kwargs)
