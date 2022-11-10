import pytest
from rest_framework.exceptions import ValidationError

from universium_test.movies.api.serializer import ActorSerializer, MovieSerializer

pytestmark = pytest.mark.django_db


class TestSerializer:
    def test_movieserializer(self):
        moviedata = {"name": " Train: An Immigrant Journey", "year": 2022}
        serializer = MovieSerializer(data=moviedata)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as err:
            print(err)
        assert serializer.is_valid()

    def test_actorserializer(self):
        actordata = {"first_name": "John", "last_name": "Doe", "gender": "M"}
        serializer = ActorSerializer(data=actordata)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as err:
            print(err)

        assert serializer.is_valid()
