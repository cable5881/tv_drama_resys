from django.conf import settings
from django.db import models

from meiju.models.drama import Drama


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='reviews',
        on_delete=models.CASCADE,
    )
    drama = models.ForeignKey(
        Drama,
        related_name='reviews',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True, default='')
    content = models.TextField(blank=True, null=True, default='')
    rating = models.PositiveSmallIntegerField(default=0)
    pubtime = models.DateTimeField(auto_now=True)
    is_watched = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ('created',)
