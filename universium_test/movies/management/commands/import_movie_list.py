import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from universium_test.movies.models import Movie


class Command(BaseCommand):
    help = "Import Movies from .csv file"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **options):
        csv_path = settings.ROOT_DIR / "data" / options["name"]
        ID = 0
        NAME = 1
        YEAR = 2
        RANK = 3
        with open(csv_path, encoding="utf8") as f:
            movies = csv.reader(f)
            for index, movie in enumerate(movies):
                if index == 0:
                    if movie[RANK].lower() != "rank":
                        raise ValueError("This is not Movies File")
                    else:
                        continue
                Movie(
                    id=movie[ID],
                    name=movie[NAME],
                    year=movie[YEAR],
                    rank=None if movie[RANK] == "" else movie[RANK],
                ).save()
