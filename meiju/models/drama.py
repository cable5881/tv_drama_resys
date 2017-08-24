from django.db import models

from meiju.models.drama_type import DramaType


class Drama(models.Model):
    title_cn = models.CharField(max_length=200, null=True, blank=True)
    image = models.URLField()
    title_en = models.CharField(max_length=200)
    # duration = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    episodes = models.PositiveSmallIntegerField()
    summary = models.TextField(blank=True, null=True)
    types = models.ManyToManyField(DramaType, related_name='types')
    douban_url = models.URLField(null=True, blank=True)
    seasons_count = models.PositiveSmallIntegerField(default=1)
    current_season = models.PositiveSmallIntegerField(default=1)
    alternate_name = models.CharField(max_length=200, null=True, blank=True)
    avg_rating = models.DecimalField(default=0, max_digits=8, decimal_places=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_en

    # class Meta:
    #     ordering = ('created',)
