from courses.models import Lecture, Homework
from rest_framework import serializers


class LectureCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = "__all__"
        extra_kwargs = {
            "date_created": {"read_only": True}
        }


class LectureDetailSerializer(serializers.ModelSerializer):
    homework = serializers.SerializerMethodField('has_homework')

    def has_homework(self, lecture):
        try:
            return Homework.objects.get(lecture=lecture.id).id
        except:
            return "None"

    class Meta:
        model = Lecture
        fields = ("id", "course", "topic", "file", "date_created", "homework")
        extra_kwargs = {
            "date_created": {"read_only": True},
            "course": {"read_only": True},
            "homework": {"read_only": True},
        }


class LecturesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = ("id", "topic", "file", "date_created")
