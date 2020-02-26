from .models import Course
from rest_framework import serializers


class CourseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"
        extra_kwargs = {
            "author": {
                "read_only": True
            }
        }

    def create(self, validated_data):
        if 'author' not in validated_data:
            validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class CoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

# class UserRegistrationSerializer(UserCreateSerializer):
#     """Create user and add profiles to it"""
#     USER_TYPES = Choices("Student", "Teacher")
#     user_type = serializers.ChoiceField(choices=USER_TYPES)
#
#     def create(self, validated_data):
#         user = super().create(validated_data)
#         print(validated_data)
#         if validated_data["user_type"] == "Teacher":
#             teacher = Teacher.objects.create(
#                 user=user
#             )
#             teacher.save()
#             print("1")
#         elif validated_data["user_type"] == "Student":
#             student = Student.objects.create(
#                 user=user
#             )
#             student.save()
#         return user
