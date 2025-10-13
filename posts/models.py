from django.db import models
from rest_framework.authentication import get_user_model

# Create your models here.

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    post_image = models.ImageField(upload_to='post_image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="post_comments", on_delete=models.CASCADE)
    author = models.ForeignKey(Post, related_name="author_comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} commented on {self.post}'
    
class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} likes {self.post}'
