from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Blog, User_Like_Blog
from .serializers import UserSerializer, BlogSerializer, UserLikeBlogSerializer
from django.db.models import Count


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogListCreate(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class BlogLike(generics.CreateAPIView):
    queryset = User_Like_Blog.objects.all()
    serializer_class = UserLikeBlogSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self,serializer):
        serializer.save(user = self.request.user)

class BlogList(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        queryset = Blog.objects.annotate(likes_count = Count('userlikeblog'))
        return queryset


