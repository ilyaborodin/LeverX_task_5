from .models import Student, Teacher
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from model_utils import Choices


class UserRegistrationSerializer(UserCreateSerializer):
    """Create user and add profiles to it"""
    USER_TYPES = Choices("Student", "Teacher")
    user_type = serializers.ChoiceField(choices=USER_TYPES)

    def create(self, validated_data):
        user = super().create(validated_data)
        print(validated_data)
        if validated_data["user_type"] == "Teacher":
            teacher = Teacher.objects.create(
                user=user
            )
            teacher.save()
            print("1")
        elif validated_data["user_type"] == "Student":
            student = Student.objects.create(
                user=user
            )
            student.save()
        return user
