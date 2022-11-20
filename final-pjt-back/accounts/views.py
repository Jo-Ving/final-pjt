from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

from django.contrib.auth import login as auth_login
from django.contrib import auth

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    password = request.data.get('password')

    if serializer.is_valid(raise_exception=True):
        if serializer.validated_data.get('password') == serializer.validated_data.get('password_confirm'):
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    pass
    # serializer = UserSerializer(data=request.data)
    # print(request.data,'👍')
    # email = request.data.get('email')
    # password = request.data.get('password')
    # print(password,'🔮🔮🔮🔮🔮🔮')
    # user = auth.authenticate(
        # request,email =email
    # )
    # print(user)


    # return Response(status = status.HTTP_201_CREATED)
    # if request.user.is_authenticated:
        # print('🤴🤴🤴🤴🤴🤴🤴')
    
    # auth_login(request.data,)
    # return Response(status=status.HTTP_201_CREATED)

    

