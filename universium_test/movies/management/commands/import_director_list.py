import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from universium_test.movies.models import Director


class Command(BaseCommand):
    help = "Import Directors from .csv file"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **options):
        csv_path = settings.ROOT_DIR / "data" / options["name"]
        ID = 0
        FIRST_NAME = 1
        LAST_NAME = 2
        with open(csv_path, encoding="utf8") as f:
            directors = csv.reader(f)
            for index, director in enumerate(directors):
                if index == 0:
                    if director[FIRST_NAME].lower() != "first_name":
                        raise ValueError("This is not Actors File")
                    else:
                        continue
                Director(
                    id=director[ID],
                    first_name=director[FIRST_NAME],
                    last_name=director[LAST_NAME],
                ).save()
