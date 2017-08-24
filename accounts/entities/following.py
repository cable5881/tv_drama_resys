from django.db.models import Model
from django.conf import settings
from django.db import models


class Following(Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='followings',
        on_delete=models.CASCADE,
    )

    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
