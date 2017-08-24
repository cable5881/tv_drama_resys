from django.contrib import admin

from meiju.models.cast import Cast
from meiju.models.director import Director
from meiju.models.drama import Drama
from meiju.models.drama_type import DramaType

admin.site.register(Drama)
admin.site.register(Director)
admin.site.register(DramaType)
admin.site.register(Cast)
