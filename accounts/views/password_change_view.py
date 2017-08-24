from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from tv_drama_resys import settings


class PasswordChangeView(LoginRequiredMixin, FormView):
    template_name = 'user/password_change.html'
    form_class = PasswordChangeForm
    success_url = settings.INDEX_URL

    # PasswordChangeView的init方法需要user参数
    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
        })
        return kwargs

    def form_valid(self, form):
        form.save(commit=True)
        return super(PasswordChangeView, self).form_valid(form)
