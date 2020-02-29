from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import comments_serializers
from courses.permissions.comments_permissions import IsParticipantId, IsParticipantPk
from courses.models import Comment
from rest_framework.response import Response


@permission_classes((IsAuthenticated, IsParticipantId))
class CommentCreateView(generics.CreateAPIView):
    serializer_class = comments_serializers.CommentCreateSerializer


@permission_classes((IsAuthenticated, IsParticipantPk))
class CommentListView(generics.ListAPIView):
    serializer_class = comments_serializers.CommentListSerializer

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(assessment=kwargs["pk"])

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(*args, **kwargs))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)