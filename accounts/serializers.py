from rest_framework import serializers
from rest_framework.authentication import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2', 'token']

    def validate(self, attrs):
        """Validating that the two passwords are the same"""
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError("Passwords not matching")
        return attrs
    
    def create(self, validated_data):
        """Create a user instance upon registration"""
        validated_data.pop('password2') # pop the password2 since it is not needed in db
        # Using the get_user_model() instead of User
        user = get_user_model().objects.create_user(**validated_data) # Create a user. Passes the validated data to the required fields
        # Create a token for the user
        Token.objects.create(user = user)
        return user
    
    def get_token(self, obj):
        """Return the token needed in the serializer response"""
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'following']


        