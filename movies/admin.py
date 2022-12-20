from django.contrib import admin

from movies.models import *
# Register your models here.

admin.site.register(Movies)
admin.site.register(ScoreMovie)
admin.site.register(ViewMovie)

