import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from universium_test.movies.models import Actor


class Command(BaseCommand):
    help = "Import Actors from .csv file"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **options):
        csv_path = str(settings.ROOT_DIR / "data" / options["name"])
        ID = 0
        FIRST_NAME = 1
        LAST_NAME = 2
        GENDER = 3
        with open(csv_path, encoding="utf8") as f:
            actors = csv.reader(f)
            for index, actor in enumerate(actors):
                if index == 0:
                    if actor[GENDER].lower() != "gender":
                        raise ValueError("This is not Actors File")
                    else:
                        continue
                Actor(
                    id=actor[ID],
                    first_name=actor[FIRST_NAME],
                    last_name=actor[LAST_NAME],
                    gender=actor[GENDER],
                ).save()
