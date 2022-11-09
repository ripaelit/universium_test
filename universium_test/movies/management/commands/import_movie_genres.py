import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from universium_test.movies.models import Movie, MovieGenre


class Command(BaseCommand):
    help = "Import Movies Genres from .csv file"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **options):
        csv_path = settings.ROOT_DIR / "data" / options["name"]
        MOVIE = 0
        GENRE = 1
        with open(csv_path, encoding="utf8") as f:
            movie_genres = csv.reader(f)
            for index, movie_genre in enumerate(movie_genres):
                if index == 0:
                    if movie_genre[GENRE].lower() != "genre":
                        raise ValueError("This is not Movies Genres File")
                    else:
                        continue
                try:
                    movie = Movie.objects.get(pk=movie_genre[MOVIE])
                except Movie.DoesNotExist:
                    continue
                MovieGenre(
                    movie=movie,
                    genre=movie_genre[GENRE],
                ).save()
