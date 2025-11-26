# core/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile, Post

User = get_user_model()  # <- this is your custom User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'location', 'birth_date', 'avatar']
        read_only_fields = ['user']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'description', 'created_at', 'updated_at', 'is_public']
        read_only_fields = ['user', 'created_at', 'updated_at']

