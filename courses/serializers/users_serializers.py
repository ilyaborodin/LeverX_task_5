from courses.models import User
from rest_framework import serializers
from django.contrib.auth import password_validation


class UserRegistrationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_password(self, data):
        password_validation.validate_password(password=data, user=User)
        return data

    class Meta:
        model = User
        fields = ("id", "username", "email", "user_type", "password")
        extra_kwargs = {
            "password": {"write_only": True}
        }


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")
