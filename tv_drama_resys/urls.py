"""tv_drama_resys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# Create a router and register our viewsets with it.
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from accounts.views.user_view import UserViewSet
from meiju.views.drama_view import DramaViewSet

# router = DefaultRouter()
# router.register(r'dramas', DramaViewSet)
# router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.


urlpatterns = [
    # url(r'^', include(router.urls)),
    # url('^', include('django.contrib.auth.urls')),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('accounts.urls')),
    url(r'^', include('meiju.urls')),
    url(r'^', include('reviews.urls')),
    url(r'^', include('space.urls')),
    url(r'^', include('home.urls')),
    url(r'^', include('data_visualization.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
