from django.db import models

from meiju.models.drama import Drama


class Writer(models.Model):
    drama = models.ForeignKey(Drama, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.drama.title_en + ' : ' + self.name
