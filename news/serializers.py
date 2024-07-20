from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, User_Like_Blog

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['id' , 'username' ,'password']
        extra_kwargs = {'password' : {'write_only' : True}}
        
        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user
        

class BlogSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)


    class Meta():
        model = Blog
        fields = ['id' , 'title' , 'content' , 'author' , 'created_at']

class UserLikeBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Like_Blog
        fields = ['id', 'user', 'blog', 'liked_at']
