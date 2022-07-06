from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=3)
    last_name = models.CharField(max_length=3)
    birth = models.DateField()
    movie = models.ManyToManyField('Movie')


    class Meta:
        db_table = 'actors'


class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    running_time = models.IntegerField()


    class Meta:
        db_table = 'movies'     