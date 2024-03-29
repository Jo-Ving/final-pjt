from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('username', 'like_movies',)
        read_only_fields = ('like_movies',)
