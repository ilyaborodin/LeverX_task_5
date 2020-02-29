from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import lectures_serializers
from courses.permissions.lectures_permissions import IsParticipantObj, IsParticipantID, IsParticipantPK
from courses.models import Course, Lecture
from rest_framework.response import Response


@permission_classes((IsAuthenticated, IsParticipantID))
class LectureCreateView(generics.CreateAPIView):
    """
    Create Lecture
    Available for teachers of this course
    """
    serializer_class = lectures_serializers.LectureCreateSerializer


@permission_classes((IsAuthenticated, IsParticipantObj))
class LectureDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve lecture for students of this course
    Retrieve/Update/Destroy lecture for teachers of this course
    Available for teachers, students
    """
    serializer_class = lectures_serializers.LectureDetailSerializer
    queryset = Lecture.objects.all()


@permission_classes((IsAuthenticated, IsParticipantPK))
class LecturesListView(generics.ListAPIView):
    """
    Retrieve list of lectures
    Available for teachers, students of this course
    """
    serializer_class = lectures_serializers.LecturesListSerializer

    def get_queryset(self, *args, **kwargs):
        return Lecture.objects.filter(course=kwargs["pk"])

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(*args, **kwargs))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

