import pytest
from django.test import RequestFactory
from django.urls.base import reverse
from rest_framework import status
from rest_framework.test import RequestsClient

from universium_test.movies.models import Movie

pytestmark = pytest.mark.django_db


class TestMovie:
    def test_movie_list(self, rf: RequestFactory, movies, client: RequestsClient):
        response = client.get(reverse("movie-list"))
        assert response.status_code == status.HTTP_200_OK
        assert len(Movie.objects.all()) == 4

    def test_actor_stats(self, rf: RequestFactory, actor, client: RequestsClient):
        response = client.get(reverse("actor-detail", args=[actor.pk]))
        assert response.status_code == status.HTTP_200_OK
