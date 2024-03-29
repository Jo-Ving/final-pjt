from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    password = request.data.get('password')

    if serializer.is_valid(raise_exception=True):
        if serializer.validated_data.get('password') == serializer.validated_data.get('password_confirm'):
            user = serializer.save()
            user.set_password(password)
            user.save()

            # token 접근
            token = TokenObtainPairSerializer.get_token(user)
            print(token,'💝💝💝💝💝💝💝💝💝')
            refresh_token = str(token)
            access_token = str(token.access_token)

            return Response({
                'user':serializer.data,
                'message':'register success',
                'token':{
                    'access':access_token,
                    'refresh':refresh_token
                }
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    print(request.data,'💦💦💦💦💦💦💦💦💦💦')
    user = authenticate(
        email = request.data.get('email'), password = request.data.get('password')
    )
    print(user,'💥💥💥💥💥💥💥💥💥💥💥')


@api_view(['GET'])
def profile(request):
    movies = Movie.objects.filter(like_users = request.user)
    print(request.user)
    print(movies,'💥💥💥')
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)