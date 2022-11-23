from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    pick_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='pick_movies')    
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    backdrop_path = models.CharField(max_length=200, null=True)
    overview = models.TextField()
    genres = models.ManyToManyField(Genre ,related_name='genre_movies')

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    review_score = models.FloatField()

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

