from django.views.generic import FormView

from accounts import models
from accounts.forms.sign_up_form import MyCustomedUserCreationForm
from tv_drama_resys import settings


class SignUpView(FormView):
    template_name = 'home/sign_up.html'
    form_class = MyCustomedUserCreationForm
    success_url = settings.LOGIN_URL

    def get_context_data(self, **kwargs):
        kwargs = super(SignUpView, self).get_context_data()
        kwargs['sexes'] = models.MyUser.SEX_CHOICES
        return kwargs

    def form_valid(self, form):
        form.save(commit=True)
        return super(SignUpView, self).form_valid(form)
