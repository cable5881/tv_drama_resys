from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from accounts.entities.my_user_manager import MyUserManager


class MyUser(AbstractBaseUser):
    BOY = 'B'
    GIRL = 'G'
    UNKNOWN = 'U'
    SEX_CHOICES = (
        (BOY, '男生'),
        (GIRL, '女生'),
        (UNKNOWN, '保密'),
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # profile = models.FilePathField(path="/accounts/views/profile", match="*.jpg", recursive=True)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=UNKNOWN,
    )
    date_of_birth = models.DateField(null=True)
    nickname = models.CharField(max_length=200)
    city = models.CharField(max_length=200, null=True, blank=True)
    introduction = models.CharField(max_length=200, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    login_days = models.IntegerField(default=1)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    # 控制台添加所需字段
    REQUIRED_FIELDS = ['nickname']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        app_label = 'accounts'
