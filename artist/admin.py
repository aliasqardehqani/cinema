from django.contrib import admin
# Register your models here.
from .models import Horror_genre, Action

class Adminmode(admin.ModelAdmin):
    list_display = ['movie_name', 'best_movie_actor', 'actor_fav']
    search_fields = ['movie_name', 'best_movie_actor']


admin.site.register(Horror_genre, Adminmode)
admin.site.register(Action, Adminmode)
