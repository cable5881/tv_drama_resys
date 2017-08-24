from datetime import datetime, timedelta

from django.contrib.auth import login
from django.utils import timezone
from django.views.generic import FormView

from accounts.forms.login_form import AuthenticationFormWithoutAdmin
from tv_drama_resys import settings


class LoginView(FormView):
    template_name = 'home/sign_in.html'
    form_class = AuthenticationFormWithoutAdmin
    redirect_authenticated_user = True
    success_url = settings.INDEX_URL

    # 如果表单提交正确则在转发到首页前执行这个函数
    def form_valid(self, form):
        user = form.get_user()
        now = timezone.now()
        if now.day - user.last_login.day >= 1:
            user.login_days += 1
        user.last_login = now
        user.save()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)
