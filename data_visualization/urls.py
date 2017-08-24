from django.conf.urls import url

from data_visualization import views

app_name = 'data_visualization'

urlpatterns = [
    url(r'^visual/$', views.visual, name='visual'),
    url(r'^visual/getSexs$', views.getSexs, name='get_sexs'),
]

