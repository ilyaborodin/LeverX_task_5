from courses.models import Course
from rest_framework import serializers


class CourseDetailSerializer(serializers.ModelSerializer):

    def validate_students(self, attrs):
        return validator_many_to_many(attrs, "Student")

    def update(self, instance, validated_data):
        add_remove_user(instance, validated_data, "students")
        instance.save()
        return instance

    class Meta:
        model = Course
        fields = ("id", "title", "description", "date_created", "creator", "teachers", "students")
        extra_kwargs = {
            "title": {"read_only": True},
            "description": {"read_only": True},
            "date_created": {"read_only": True},
            "creator": {"read_only": True},
            "teachers": {"read_only": True},
        }


class CreatorCourseDetailSerializer(serializers.ModelSerializer):

    def validate_students(self, attrs):
        return validator_many_to_many(attrs, "Student")

    def validate_teachers(self, attrs):
        return validator_many_to_many(attrs, "Teacher")

    def update(self, instance, validated_data):
        add_remove_user(instance, validated_data, "students")
        add_remove_user(instance, validated_data, "teachers")
        self.add_creator_to_teachers(validated_data, instance)
        return super().update(instance, validated_data)

    def create(self, validated_data):
        if 'creator' not in validated_data:
            validated_data['creator'] = self.context['request'].user
        self.add_creator_to_teachers(validated_data)
        return super().create(validated_data)

    def add_creator_to_teachers(self, validated_data, instance=None):
        if instance is None or "teachers" in validated_data and instance.creator not in validated_data["teachers"]:
            validated_data["teachers"].append(self.context['request'].user)
        return validated_data

    class Meta:
        model = Course
        fields = "__all__"
        extra_kwargs = {
            "creator": {
                "read_only": True
            }
        }


class CoursesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"
        # fields = ("id", "title", "description", "date_created", "creator")


def validator_many_to_many(attrs, user_type):
    """validator for students and teachers"""
    if len(attrs) != len(set(attrs)):
        raise serializers.ValidationError('All users must be unique.')
    for teacher in attrs:
        if teacher.user_type != user_type:
            raise serializers.ValidationError('All users must be {}s.'.format(user_type.lower()))
    return attrs


def add_remove_user(instance, validated_data, user_type):
    """add or remove users from teachers, students fields"""
    if user_type in validated_data:
        if user_type == "students":
            field = instance.students
        else:
            field = instance.teachers
        for user in validated_data[user_type]:
            if user == instance.creator:
                continue
            if user in field.all():
                field.remove(user)
            else:
                field.add(user)
        del validated_data[user_type]
