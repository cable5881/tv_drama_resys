from django.db.models import Q
from django.views.generic import DetailView
from django.views.generic import ListView

from meiju.models.drama import Drama
from meiju.models.drama_type import DramaType
from reviews.models.review import Review
from tv_drama_resys import settings
from utils import recommender


class DramaDetailView(DetailView):
    model = Drama
    template_name = 'drama/drama_detail.html'

    def similarItems(self, drama):
        return recommender.calculateSimilarItems(self.dramas_rating_set(drama))

    def dramas_rating_set(self, drama):
        drama_set = {}
        dramas = Drama.objects.all()

        for d in dramas:
            if d.id == drama.id or (d.reviews.all().exists() and not d.reviews.filter(user=self.request.user, is_watched=True).exists()):
                user_rating_set = {}
                for r in d.reviews.all():
                    user_rating_set[r.user_id] = r.rating
                drama_set[d.id] = user_rating_set

        return drama_set

    def getSomeTypedUnwatchedDramasOrderByYearRating(self, user, drama, num=6):
        watched_reviews = user.reviews.filter(is_watched=True).all()
        unwatched_dramas = Drama.objects.exclude(id=drama.id).filter(types__in=drama.types.all()).exclude(
            reviews__in=watched_reviews).distinct().order_by('-year', '-avg_rating')[0:num]
        return unwatched_dramas

    def getUserRatings(self, user):
        reviews = user.reviews.all()
        user_ratings = {}

        for review in reviews:
            user_ratings[review.drama_id] = review.rating

        return user_ratings

    def getFixedRecmd_dramas(self, r_dramas, user, drama):
        length = len(r_dramas)
        if length < 6:
            num = 6 - length

            for d in self.getSomeTypedUnwatchedDramasOrderByYearRating(user, drama, num):
                r_dramas.append(d)

        return r_dramas

    def render_to_response(self, context, **response_kwargs):
        user = self.request.user
        if user.is_authenticated:
            drama = context['object']
            recmd_dramas = []
            if drama.reviews.count() < 5:
                for item in self.getSomeTypedUnwatchedDramasOrderByYearRating(user, drama):
                    recmd_dramas.append(item)
            else:
                for item in self.similarItems(drama)[drama.id]:
                    recmd_dramas.append(Drama.objects.get(pk=item[1]))
                recmd_dramas = self.getFixedRecmd_dramas(recmd_dramas, user, drama)

            context['recmd_dramas'] = recmd_dramas

            current_user_review = drama.reviews.filter(user=self.request.user)
            if current_user_review:
                context['current_user_review'] = current_user_review.get()

            reviews_with_content = drama.reviews.exclude(Q(title=None) | Q(title=''))
            if reviews_with_content:
                context['reviews'] = reviews_with_content.all()[:5]

        return super(DramaDetailView, self).render_to_response(context, **response_kwargs)


class SearchDramaView(ListView):
    template_name = 'home/search.html'
    paginate_by = settings.OBJECTS_NUM_PER_PAGE

    def get_queryset(self):
        key = self.kwargs['search_text']
        self.queryset = Drama.objects.filter(
            Q(title_cn__contains=key) |
            Q(title_en__contains=key) |
            Q(alternate_name__contains=key)
        ).order_by('-year', '-avg_rating')

        return super(SearchDramaView, self).get_queryset()

    def render_to_response(self, context, **response_kwargs):
        context['search_text'] = self.kwargs['search_text']
        return super(SearchDramaView, self).render_to_response(context, **response_kwargs)


class CategoryDramaView(ListView):
    template_name = 'home/category.html'
    paginate_by = settings.OBJECTS_NUM_PER_PAGE

    def get_queryset(self):
        if 'type' in self.request.GET:
            type_db = DramaType.objects.filter(pk=self.request.GET['type'])
            self.queryset = Drama.objects.filter(types=type_db)
        else:
            self.queryset = Drama.objects.all()

        if 'order' in self.request.GET:
            self.queryset = self.queryset.order_by('-' + self.request.GET['order'])
        else:
            self.queryset = self.queryset.order_by('-year')

        return super(CategoryDramaView, self).get_queryset()

    def render_to_response(self, context, **response_kwargs):
        page_args_str = None
        if 'type' in self.request.GET:
            kind = self.request.GET['type']
            page_args_str = '&type=' + kind
            context['type'] = int(kind)
        if 'order' in self.request.GET:
            order = self.request.GET['order']
            if page_args_str:
                page_args_str = page_args_str + '&order=' + order
            else:
                page_args_str = '&order=' + order

            context['order'] = self.request.GET['order']

        context['page_args_str'] = page_args_str
        context['types'] = DramaType.objects.all()
        return super(CategoryDramaView, self).render_to_response(context, **response_kwargs)
