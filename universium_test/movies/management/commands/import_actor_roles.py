import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from universium_test.movies.models import Actor, ActorRole, Movie


class Command(BaseCommand):
    help = "Import Actor Roles from .csv file"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **options):
        csv_path = settings.ROOT_DIR / "data" / options["name"]
        ACTOR = 0
        MOVIE = 1
        ROLE = 2
        with open(csv_path, encoding="utf8") as f:
            roles = csv.reader(x.replace("\0", " ") for x in f)
            for index, role in enumerate(roles):
                if index == 0:
                    if role[ROLE].lower() != "role":
                        raise ValueError("This is not Roles File")
                    else:
                        continue
                try:
                    actor = Actor.objects.get(pk=role[ACTOR])
                except Actor.DoesNotExist:
                    continue
                try:
                    movie = Movie.objects.get(pk=role[MOVIE])
                except Movie.DoesNotExist:
                    continue

                print(role)
                ActorRole(
                    actor=actor,
                    movie=movie,
                    role=None if role[ROLE] == "" else role[ROLE],
                ).save()
