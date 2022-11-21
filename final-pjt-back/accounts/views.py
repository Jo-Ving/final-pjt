from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

from django.contrib.auth import login as auth_login, authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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


@api_view(['POST'])
def profile(request):
    # User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return Response(request, 'accounts/profile.html', context)
