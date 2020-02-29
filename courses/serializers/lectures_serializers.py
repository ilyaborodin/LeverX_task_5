from courses.models import Lecture
from rest_framework import serializers


class LectureCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = "__all__"
        extra_kwargs = {
            "date_created": {"read_only": True}
        }


class LectureDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = "__all__"
        extra_kwargs = {
            "date_created": {"read_only": True},
            "course": {"read_only": True}
        }


class LecturesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = ("id", "topic", "file", "date_created")
