from django.conf.urls import url
from django.contrib.auth import views

from accounts.views import login_view
from accounts.views import password_change_view
from accounts.views import sign_up_view
from accounts.views import user_change_view
from accounts.views.user_view import UserViewSet

app_name = 'accounts'

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'^accounts/modify$', user_change_view.UserChangeView.as_view(), name='change_user'),
    url(r'^accounts/changepassword/$', password_change_view.PasswordChangeView.as_view(), name='change_password'),
    url(r'^join/$', sign_up_view.SignUpView.as_view(), name='sign_up'),
    url(r'^login/$', login_view.LoginView.as_view(), name='log_in'),
    url(r'^logout/$', views.LogoutView.as_view(), name='log_out'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
]

# urlpatterns = [
#     url(r'^users/$', user_view.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_view.UserDetail.as_view(), name='user-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
