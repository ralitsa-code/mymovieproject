from django.contrib import admin
from movies.models import Movie, Genre, Director, Actor

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'director', 'genre', 'status', 'user']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'user']
    list_filter = ['status']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'status', 'user']
    list_filter = ['status']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'status', 'user']
    list_filter = ['status']