from django.conf.urls import url
from meiju.views import drama_view
from rest_framework.urlpatterns import format_suffix_patterns

from meiju.views import tv_drama_view
from meiju.views.drama_view import DramaViewSet, DramaTypeViewSet

app_name = 'dramas'

drama_list = DramaViewSet.as_view({
    'get': 'list'
})
drama_detail = DramaViewSet.as_view({
    'get': 'retrieve'
})
type_list = DramaTypeViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    # url(r'^dramas/category/type=(?P<type>.+)/$', tv_drama_view.CategoryDramaView.as_view(), name='drama_category'),
    url(r'^dramas/category/$', tv_drama_view.CategoryDramaView.as_view(), name='drama_category'),
    url(r'^dramas/search/wd=(?P<search_text>.+)/$', tv_drama_view.SearchDramaView.as_view(), name='search_drama'),
    url(r'^dramas/(?P<pk>[0-9]+)/$', tv_drama_view.DramaDetailView.as_view(), name='drama_detail'),
    url(r'^dramas/$', drama_list, name='drama-list'),
    url(r'^drama_type/$', type_list, name='drama-type-list')
]


# urlpatterns = [
#     url(r'^dramas/$', drama_view.DramaList.as_view(), name='drama-list'),
#     url(r'^dramas/(?P<pk>[0-9]+)/$', drama_view.DramaDetail.as_view(), name='drama-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
