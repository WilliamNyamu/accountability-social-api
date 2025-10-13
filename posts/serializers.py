from rest_framework import serializers
from .models import Post, Comment, Like
from rest_framework.authentication import get_user_model

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only = True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'author_name','post_image', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['']