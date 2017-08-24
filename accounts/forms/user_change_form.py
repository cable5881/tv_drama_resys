from django.contrib.auth import get_user_model
from django.forms import ModelForm, CharField


class MyCustomedUserChangeForm(ModelForm):

    class Meta:
        model = get_user_model()
        fields = fields = ['nickname', 'introduction', 'date_of_birth', 'sex']