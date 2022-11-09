from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin

from universium_test.movies.models import (
    Actor,
    ActorRole,
    Director,
    DirectorGenre,
    Movie,
    MovieDirector,
    MovieGenre,
)

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Movie)


@register(ActorRole)
class ActorRoleAdmin(ModelAdmin):
    list_display = [
        "actor",
        "movie",
    ]


@register(DirectorGenre)
class DirectorGenreAdmin(ModelAdmin):
    list_display = [
        "director",
        "genre",
    ]


@register(MovieDirector)
class MovieDirectorAdmin(ModelAdmin):
    list_display = [
        "director",
        "movie",
    ]


@register(MovieGenre)
class MovieGenreAdmin(ModelAdmin):
    list_display = [
        "movie",
        "genre",
    ]
