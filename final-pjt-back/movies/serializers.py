from rest_framework import serializers
from .models import Movie, Review, Comment
from accounts.models import User


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

        
class ReviewListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)
            read_only_fields = ('username',)            

    user = UserSerializer()

    class Meta:
        model = Review
        fields = '__all__'
        # fields = ('content','review_score',)
        read_only_fields = ('movie', 'user','username','review_like_users')




class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        # fields = ('content','review_score',)
        read_only_fields = ('movie', 'user', 'review_like_users')




class CommentListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)
            read_only_fields = ('username',)            

    user = UserSerializer()    

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'user')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'user')                
        