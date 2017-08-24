from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AuthenticationFormWithoutAdmin(AuthenticationForm):

    def confirm_login_allowed(self, user):
        if user.is_admin:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )