from django.conf.urls import url

from space.views import follower_view
from space.views import following_view
from space.views import search_view
from space.views import space_view

app_name = 'space'

urlpatterns = [
    url(r'^space/$', space_view.SpaceView.as_view(), name='index_without_id'),
    url(r'^space/(?P<user_id>[0-9]+)/$', space_view.SpaceView.as_view(), name='index_with_id'),
    url(r'^space/(?P<user_id>[0-9]+)/following/$', following_view.FollowingView.as_view(), name='space_following'),
    url(r'^space/add_following/$', following_view.AddFollowingView.as_view(), name='add_following'),
    url(r'^space/cancel_following/$', following_view.DeleteFollowingView.as_view(), name='cancel_following'),
    url(r'^space/search/wd=(?P<search_text>.+)/$', search_view.PeopleSearchView.as_view(), name='search_people'),
    url(r'^space/(?P<user_id>[0-9]+)/follower/$', follower_view.FollowerView.as_view(), name='space_follower'),
]
