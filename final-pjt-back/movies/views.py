from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import math
from .serializers import MovieSerializer, ReviewSerializer, ReviewListSerializer, CommentSerializer, CommentListSerializer
from .models import Movie, Review, Genre

from django.contrib.auth.decorators import login_required


@api_view(['GET'])
def movie_list(request):
    # if request.user.is_authenticated:
        if request.method == 'GET':
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer1 = MovieSerializer(movie)
        genre1_id = movie.genres.all()[:1][0].id
        genre2_id = movie.genres.all()[1:2][0].id
        genre1 = Genre.objects.get(pk=genre1_id)
        genre2 = Genre.objects.get(pk=genre2_id)
        simliar_movies1 = genre1.genre_movies.all()
        simliar_movies2 = genre2.genre_movies.all()
        simliar_movies = simliar_movies1.union(simliar_movies2)
        simliar_movies = simliar_movies.all().order_by('-vote_count', '-vote_average')[:20]
        serializer2 = MovieSerializer(simliar_movies, many=True)
        data = {
            'movie' : serializer1.data,
            'simliar_movies' : serializer2.data
        }    
        return Response(data)


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
    if movie.pick_users.filter(pk=request.user.pk).exists():
        movie.pick_users.remove(request.user)
        is_picked = False
    else:
        movie.pick_users.add(request.user)    
        is_picked = True
    return Response(is_picked)

@api_view(['GET'])
def pick_list(request):
    if request.method == 'GET':
        genre = Genre.objects.get(pk=12)
        movies = Movie.objects.all().order_by('-vote_count', '-vote_average')[:100]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

## 핫, 신작
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

## 장르 추천
@api_view(['POST'])
def recommend2(request):
    # 로그인한 사용자 id
    user = request.user
    print('유저 id: ', user)
    result1 = user.like_movies.all()
    result2 = user.pick_movies.all()
    counts_by_genre = dict()

    if result1:
        for movie in result1:
            genres = movie.genres.all()
            for genre in genres:
                counts_by_genre[genre.id] = counts_by_genre.get(genre.id, 0) + 1

    if result2:
        for movie in result2:
            genres = movie.genres.all()
            for genre in genres:
                counts_by_genre[genre.id] = counts_by_genre.get(genre.id, 0) + 1        
    # 정렬 로직
    sorted_counts_by_genre = sorted(counts_by_genre.items(), key= lambda item:item[1], reverse=True)
    print(sorted_counts_by_genre)
    if len(sorted_counts_by_genre) >= 2:
        res = sorted_counts_by_genre[:2]
        total = res[0][1] + res[1][1]
        r1 = math.ceil(res[0][1] / total * 20)
        r2 = 20-r1
        print(r1, r2)
        genre_id1, genre_id2 = res[0][0], res[1][0]
        genre1 = Genre.objects.get(pk=genre_id1)
        genre2 = Genre.objects.get(pk=genre_id2)
        genre1_movies = genre1.genre_movies.all().order_by('-vote_count', '-vote_average')
        genre2_movies = genre2.genre_movies.all().order_by('-vote_count', '-vote_average')
        genre_video1 = genre1_movies[:min(len(genre1_movies), r1*2)]
        genre_video2 = genre2_movies[:min(len(genre1_movies), r2*2)]
        genre_video = set(list(genre_video1) + list(genre_video2))
    else:
        res = sorted_counts_by_genre[0]
        genre_id1 = res[0][0]
        genre1 = Genre.objects.get(pk=genre_id1)
        genre1_movies = genre1.genre_movies.all().order_by('-vote_count', '-vote_average')
        genre_video = genre1_movies[:min(len(genre1_movies), 20)]
    print(genre_video)

    serializer = MovieSerializer(list(genre_video), many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def comment_list(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        comments = review.movie_reviews.all()
        serializer = CommentListSerializer(comments, many=True)
        print(comments)
        # reviews = get_list_or_404(Review)
        return Response(serializer.data)

    elif request.method == 'POST':
        # review = review.objects.get(pk=review_pk)
        # movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)        
        return Response(serializer.data, status=status.HTTP_201_CREATED)     

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