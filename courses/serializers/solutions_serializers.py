from courses.models import Solution
from rest_framework import serializers


class SolutionCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        if 'creator' not in validated_data:
            validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Solution
        fields = "__all__"
        extra_kwargs = {
            "creator": {"read_only": True},
            "date_created": {"read_only": True}
        }


class SolutionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = "__all__"
        extra_kwargs = {
            "date_created": {"read_only": True},
            "homework": {"read_only": True},
            "creator": {"read_only": True},
        }


class SolutionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = ("id", "homework", "link", "date_created")
