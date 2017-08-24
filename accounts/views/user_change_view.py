from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.http import JsonResponse
from django.views import View
from django.views.generic import FormView
from django.views.generic.edit import FormMixin

from accounts.forms.user_change_form import MyCustomedUserChangeForm


class UserAjaxableResponseMixin(object):
    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return Http404("User Change Failed!")

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).

        user = form.save(commit=False)
        user.id = self.request.user.id
        user.save(force_update=True, update_fields=form.fields)

        if self.request.is_ajax():
            data = {
                'msg': '保存成功！',
            }
            return JsonResponse(data)
        else:
            return Http404("User Change Failed!")


class UserChangeView(LoginRequiredMixin, UserAjaxableResponseMixin, FormMixin, View):
    form_class = MyCustomedUserChangeForm

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
