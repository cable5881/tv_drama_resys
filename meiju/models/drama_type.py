from django.db import models


class DramaType(models.Model):
    type = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'meiju_type'

    def __str__(self):
        return self.type
