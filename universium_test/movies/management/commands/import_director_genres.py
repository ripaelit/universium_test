import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from universium_test.movies.models import Director, DirectorGenre


class Command(BaseCommand):
    help = "Import Director Genres from .csv file"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **options):
        csv_path = settings.ROOT_DIR / "data" / options["name"]
        DIRECTOR = 0
        GENRE = 1
        PROB = 2
        with open(csv_path, encoding="utf8") as f:
            director_genres = csv.reader(f)
            for index, director_genre in enumerate(director_genres):
                if index == 0:
                    if director_genre[PROB].lower() != "prob":
                        raise ValueError("This is not Roles File")
                    else:
                        continue
                try:
                    director = Director.objects.get(pk=director_genre[DIRECTOR])
                except Director.DoesNotExist:
                    continue

                DirectorGenre(
                    director=director,
                    genre=director_genre[GENRE],
                    prob=director_genre[PROB],
                ).save()
