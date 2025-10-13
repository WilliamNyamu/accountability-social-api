from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.authentication import get_user_model
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response (
            {
                'error': 'username and password cannot be blank'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username=username, password=password)

    if user:
        token, _  = Token.objects.get_or_create(user = user)
        return Response (
            {
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'message': 'Sign in successfull'
            },
            status=status.HTTP_200_OK
        )
    return Response (
        {
            'error': 'Invalid credentials.'
        },
        status=status.HTTP_404_NOT_FOUND
    )

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response (
            {
                'error': 'User does not exist'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if request.user == user_to_follow:
        return Response (
            {
                'error': 'You cannot follow yourself'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if request.user.following.filter(id=user_to_follow.id).exists():
        return Response(
            {
                'error': 'You already follow this user'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    request.user.following.add(user_to_follow)
    return Response(
        {
            'message': f"You are following {user_to_follow.username}"
        },
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(
            {
                'error': 'User not found'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.user == user_to_unfollow:
        return Response(
            {
                'error': 'You cannot follow nor unfollow yourself'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    if not user_to_unfollow.followers.filter(id=request.user.id).exists():
        return Response(
            {
                'error': 'You had not followed this user'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    request.user.following.remove(user_to_unfollow)
    return Response(
        {
            'message': f'You have unfollowed {user_to_unfollow.username}'
        },
        status=status.HTTP_200_OK
    )
    