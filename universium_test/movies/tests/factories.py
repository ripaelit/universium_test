from factory import Faker
from factory.django import DjangoModelFactory

from universium_test.movies.models import Actor, Movie


class MovieFactory(DjangoModelFactory):
    name = Faker("name")

    class Meta:
        model = Movie


class ActorFactory(DjangoModelFactory):
    first_name = Faker("name")
    last_name = Faker("name")
    gender = "Male"

    class Meta:
        model = Actor
