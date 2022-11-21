from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie, Review

from django.contrib.auth.decorators import login_required


@api_view(['GET', 'POST'])
def movie_list(request):
    # if request.user.is_authenticated:
        if request.method == 'GET':
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
        # else:
        #     serializer = MovieSerializer(data=request.data)
        #     if serializer.is_valid(raise_exception=True):
        #         serializer.save(user = request.user)
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    # review = review.objects.get(pk=review_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        # print(serializer.data)
        return Response(serializer.data)
    
    # elif request.method == 'DELETE':
    #     movie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # elif request.method == 'PUT':
    #     serializer = MovieSerializer(movie, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        # reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    # review = review.objects.get(pk=review_pk)
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
def review_create(request, movie_pk):
    if request.method == 'POST':
        # review = review.objects.get(pk=review_pk)
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)

