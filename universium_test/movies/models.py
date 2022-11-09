from django.db import models
from django.utils.translation import gettext_lazy as _


class Actor(models.Model):
    class Gender(models.TextChoices):
        Male = "M"
        Female = "F"

    first_name = models.CharField(
        _("Firstname"),
        null=False,
        blank=False,
        max_length=100,
    )
    last_name = models.CharField(
        _("Lastname"),
        null=False,
        blank=False,
        max_length=100,
    )
    gender = models.CharField(
        _("Gender"),
        choices=Gender.choices,
        max_length=6,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Director(models.Model):
    first_name = models.CharField(
        _("Fisrtname"),
        null=False,
        blank=False,
        max_length=50,
    )
    last_name = models.CharField(
        _("Lastname"),
        null=False,
        blank=False,
        max_length=50,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
    )
    year = models.IntegerField(
        null=False,
        blank=False,
    )
    rank = models.FloatField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"


class ActorRole(models.Model):
    actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )
    role = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.actor.first_name} {self.actor.last_name}"


class MovieDirector(models.Model):
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )


class MovieGenre(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )
    genre = models.CharField(null=False, blank=False, max_length=50)


class DirectorGenre(models.Model):
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
    )
    genre = models.CharField(
        null=False,
        blank=False,
        max_length=50,
    )
    prob = models.FloatField(
        null=False,
        blank=True,
    )
