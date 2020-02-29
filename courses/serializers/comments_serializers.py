from courses.models import Comment
from rest_framework import serializers


class CommentCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        if 'creator' not in validated_data:
            validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {
            "creator": {"read_only": True},
            "date_created": {"read_only": True}
        }


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("id", "comment", "creator", "date_created")
