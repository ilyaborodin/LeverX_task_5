from .models import Course, User
from rest_framework import serializers
from djoser.serializers import UserSerializer


class CourseDetailSerializer(serializers.ModelSerializer):
    teachers = serializers.PrimaryKeyRelatedField(many=True,
                                                  queryset=User.objects.all(),)

    def validate_teachers(self, attrs):
        if len(attrs) != len(set(attrs)):
            raise serializers.ValidationError('All users must be unique.')
        for teacher in attrs:
            if teacher.user_type != "Teacher":
                raise serializers.ValidationError('All users must be teachers.')
        return attrs

    def update(self, instance, validated_data):
        print(instance.user)
        if "teacher" in validated_data and instance.user not in validated_data["teachers"]:
            validated_data["teachers"].append(instance.user)
        return super().update(instance, validated_data)

    class Meta:
        model = Course
        fields = "__all__"
        extra_kwargs = {
            "user": {
                "read_only": True
            }
        }

    def create(self, validated_data):
        if 'user' not in validated_data:
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
