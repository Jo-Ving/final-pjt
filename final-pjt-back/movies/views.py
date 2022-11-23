from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieSerializer, ReviewSerializer, ReviewListSerializer
from .models import Movie, Review

from django.contrib.auth.decorators import login_required


@api_view(['GET', 'POST'])
def movie_list(request):
    # if request.user.is_authenticated:
        if request.method == 'GET':
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        reviews = movie.movie_reviews.all()
        serializer = ReviewListSerializer(reviews, many=True)
        print(reviews)
        # reviews = get_list_or_404(Review)
        return Response(serializer.data)

    elif request.method == 'POST':
        # review = review.objects.get(pk=review_pk)
        # movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)        
        return Response(serializer.data, status=status.HTTP_201_CREATED)        


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def likes(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        is_liked = False
    else:
        movie.like_users.add(request.user)
        is_liked = True
    return Response(is_liked)

@api_view(['POST'])
def picks(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.pick_users.add(request.user)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def review_likes(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.review_like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
        review_is_liked = False
    else:
        review.like_users.add(request.user)
        review_is_liked = True
    return Response(review_is_liked)

@api_view(['POST'])
def recommend1(request):
    recent_movies = Movie.objects.all().order_by('-release_date', '-vote_average')[:10] 
    hot_movies =  Movie.objects.all().order_by('-vote_count', '-vote_average')[:20]
    serializer1 = MovieSerializer(recent_movies, many=True)
    serializer2 = MovieSerializer(hot_movies, many=True)
    print(request.user)
    data = {
        'recent_movies' : serializer1.data,
        'hot_movies' : serializer2.data
    }
    
    return Response(data)


