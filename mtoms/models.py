from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "actors"


class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField(null=True, blank=True)
    running_time = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "movies"


class ActorMovies(models.Model):
    actor = models.ForeignKey(
        "Actor", related_name="actormovies", on_delete=models.CASCADE, null=True
    )
    movie = models.ForeignKey(
        "Movie", related_name="actormovies", on_delete=models.CASCADE, null=True
    )

    class Meta:
        db_table = "actormovies"