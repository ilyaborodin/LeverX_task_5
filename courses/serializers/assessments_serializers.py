from courses.models import Assessment
from rest_framework import serializers


class AssessmentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assessment
        fields = "__all__"


class AssessmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ("id", "rating")
