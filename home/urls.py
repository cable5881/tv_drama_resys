from django.conf.urls import url

from accounts.views import user_view
from home.views import basic_view

app_name = 'home'

urlpatterns = [
    # ex: /polls/
    url(r'^$', basic_view.to_index, name='index_root'),
    url(r'^index$', basic_view.to_index, name='index'),
]
