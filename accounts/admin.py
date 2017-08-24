from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.entities.follower import Follower
from accounts.entities.following import Following
from accounts.models import MyUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    # A form for creating new users. Includes all the required
    # fields, plus a repeated password.
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        # fields = ('email', 'nickname', 'date_of_birth', 'introduction', 'is_admin', 'login_days', 'last_login', 'is_active')
        fields = ()

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    # A form for updating users. Includes all the fields on
    # the user, but replaces the password field with admin's
    # password hash display field.

    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser

        # 要下面的Fields有何用?
        # fields = ('email', 'password', 'profile', 'date_of_birth', 'introduction', 'nickname', 'is_active', 'is_admin')
        fields = ()

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    # list_display = ('email', 'nickname', 'profile', 'date_of_birth', 'introduction', 'is_admin')
    list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)

    # 提供哪些需要修改的字段到change界面
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Personal info', {'fields': ('nickname', 'profile', 'date_of_birth', 'introduction')}),
    #     ('Permissions', {'fields': ('is_admin',)}),
    # )
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('nickname', 'sex', 'date_of_birth', 'introduction')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    # 提供哪些需要修改的字段到add界面
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname', 'password1', 'password2', 'introduction')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
admin.site.register(Following)
admin.site.register(Follower)
