import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from universium_test.movies.models import Director, Movie, MovieDirector


class Command(BaseCommand):
    help = "Import Movies Genres from .csv file"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **options):
        csv_path = settings.ROOT_DIR / "data" / options["name"]
        DIRECTOR = 0
        MOVIE = 1
        with open(csv_path, encoding="utf8") as f:
            movie_directors = csv.reader(f)
            for index, movie_director in enumerate(movie_directors):
                if index == 0:
                    if movie_director[DIRECTOR].lower() != "director_id":
                        raise ValueError("This is not Movies Directors File")
                    else:
                        continue
                try:
                    director = Director.objects.get(pk=movie_director[DIRECTOR])
                except Director.DoesNotExist:
                    continue
                try:
                    movie = Movie.objects.get(pk=movie_director[MOVIE])
                except Movie.DoesNotExist:
                    continue
                MovieDirector(
                    director=director,
                    movie=movie,
                ).save()
