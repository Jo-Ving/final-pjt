from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    backdrop_path = models.CharField(max_length=200)
    overview = models.TextField()
    genres = models.ManyToManyField(Genre)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


