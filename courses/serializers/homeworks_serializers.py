from rest_framework import serializers
from courses.models import Homework


class HomeworkCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = "__all__"
        extra_kwargs = {
            "date_created": {"read_only": True}
        }


class HomeworkDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = "__all__"
        extra_kwargs = {
            "date_created": {"read_only": True},
            "lecture": {"read_only": True}
        }
