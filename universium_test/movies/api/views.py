import statistics
from collections import Counter
from typing import Any

from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet

from universium_test.movies.models import Actor, ActorRole, Movie, MovieGenre

from .serializer import ActorSerializer, MovieSerializer


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer

    queryset = Movie.objects.all()

    # Set django-filter backend
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [SearchFilter]

    # Set django-filter filtering fields
    filter_fields = {
        "moviegenre__genre": ["exact", "in"],
        "moviedirector__director__first_name": ["exact", "in"],
        "moviedirector__director__last_name": ["exact", "in"],
    }

    # Set django-filter ordering fields
    ordering_fields = ["id", "moviegenre", "moviedirector", "name", "year", "rank"]


class ActorViewSet(ModelViewSet):
    def get_serializer_class(self):
        return ActorSerializer

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        instance = self.get_object()
        data = self.get_serializer(instance).data
        actor_first_name = data["first_name"]
        actor_last_name = data["last_name"]
        genre_list = []
        movie_list = []
        partner_list = []
        for role in data["actorrole_set"]:
            genre_list += list(
                MovieGenre.objects.filter(movie=role["movie"]).values("genre")
            )
            partner_list += list(
                ActorRole.objects.filter(movie=role["movie"]).values("actor")
            )
            movie_list.append(role["movie"])

        genre_list = list(map(lambda genre: genre["genre"], genre_list))

        number_of_movies = len(list(set(movie_list)))
        number_of_movies_by_genre = Counter(genre_list)

        if genre_list:
            top_genre = statistics.mode(genre_list)
        else:
            top_genre = ""

        partner_list = list(map(lambda genre: genre["actor"], partner_list))
        if partner_list:
            partner_list = [
                partner for partner in partner_list if partner != data["id"]
            ]
            top_partner_id = statistics.mode(partner_list)
        else:
            top_partner_id = None
        try:
            top_partner_first_name = getattr(
                Actor.objects.get(pk=top_partner_id), "first_name"
            )
        except Actor.DoesNotExist:
            top_partner_first_name = " "
        try:
            top_partner_last_name = getattr(
                Actor.objects.get(pk=top_partner_id), "last_name"
            )
        except Actor.DoesNotExist:
            top_partner_last_name = " "
        most_frequent_partner = {
            "id": top_partner_id,
            "name": f"{top_partner_first_name} {top_partner_last_name}",
            "number_of_shared_movies": Counter(partner_list)[top_partner_id],
        }
        response_data = {
            "id": data["id"],
            "name": f"{actor_first_name} {actor_last_name}",
            "top_genre": top_genre,
            "number_of_movies": number_of_movies,
            "number_of_movies_by_genre": number_of_movies_by_genre,
            "most_frequent_partner": most_frequent_partner,
        }
        return Response(data=response_data, status=status.HTTP_200_OK)

    queryset = Actor.objects.all()
