from rest_framework.filters import SearchFilter
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet

from universium_test.movies.models import Movie

from .serializer import MovieSerializer


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
