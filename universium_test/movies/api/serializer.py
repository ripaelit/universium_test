from rest_framework import serializers

from universium_test.movies.models import (
    Actor,
    ActorRole,
    Movie,
    MovieDirector,
    MovieGenre,
)


class MovieDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDirector
        fields = ["director"]
        depth = 3


class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = ["genre"]


class MovieSerializer(serializers.ModelSerializer):
    moviegenre_set = MovieGenreSerializer(many=True, read_only=True)
    moviedirector_set = MovieDirectorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"


class ActorRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorRole
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    actorrole_set = ActorRoleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = "__all__"
