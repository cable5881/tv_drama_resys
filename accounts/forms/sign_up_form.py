from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts import models


class MyCustomedUserCreationForm(UserCreationForm):
    # sex = forms.CharField(widget=forms.Select(
    #         choices=models.MyUser.SEX_CHOICES,
    #         attrs={'class': 'form-control'}
    # ))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email', 'sex', 'date_of_birth', 'nickname']

