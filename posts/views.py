from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework import generics
from .models import Post, Comment, Like
from rest_framework import permissions
from .permissions import IsAuthororReadOnly
# Create your views here.

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    # The perform_create() is specifically designed for injecting extra logic before saving the object.
    def perform_create(self, serializer):
        """The logged in user becomes the author automatically"""
        serializer.save(author=self.request.user)
    
    # Add a message to show success upon creation
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs) # To include everything in the Post Serializer
        # We add another field with the name message before returning the response.
        response.data['message'] = 'Post created successfully'
        return response

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthororReadOnly]

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = 'Post updated successfully'
        return response
    
class PostDestroyView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthororReadOnly]
    

