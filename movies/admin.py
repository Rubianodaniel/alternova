from django.contrib import admin

from movies.models import *
# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "type")
    search_fields = ("name", "gender", "type")
    list_filter = ("name", "gender", "type")

class ScoreAdmin(admin.ModelAdmin):
    list_display = ("name_id", "score")

class ViewsAdmin(admin.ModelAdmin):
    list_display = ("name_id", "view")


admin.site.register(Movies, MoviesAdmin)
admin.site.register(ScoreMovie, ScoreAdmin)
admin.site.register(ViewMovie, ViewsAdmin)

