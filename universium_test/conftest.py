import pytest

from universium_test.movies.models import Actor
from universium_test.movies.tests.factories import ActorFactory, MovieFactory
from universium_test.users.models import User
from universium_test.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def actor(db) -> Actor:
    return ActorFactory()


@pytest.fixture
def movies(db):
    MovieFactory.create(name="movie1", year="2022")
    MovieFactory.create(name="movie1", year="2022")
    MovieFactory.create(name="movie1", year="2022")
    MovieFactory.create(name="movie1", year="2022")
    return MovieFactory
