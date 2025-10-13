from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_phone_number

# Create your models here.

class CustomUser(AbstractUser):
    """Inherits from the User model but adds other fields"""
    bio = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to='profile_picture', blank=True, null=True)
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        unique=True,
        validators=[validate_phone_number]
        )
    following = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name="followers", 
        blank=True
    )

    def __str__(self):
        return self.username
