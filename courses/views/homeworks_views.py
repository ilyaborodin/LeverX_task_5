from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import homeworks_serializers
from courses.permissions.lectures_permissions import IsParticipantObj, IsParticipantID
from courses.models import Homework


@permission_classes((IsAuthenticated, IsParticipantID))
class LectureCreateView(generics.CreateAPIView):
    """
    Create homework
    Available for teachers of this course
    """
    serializer_class = homeworks_serializers.LectureCreateSerializer


@permission_classes((IsAuthenticated, IsParticipantObj))
class LectureDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve homework for students of this course
    Retrieve/Update/Destroy homework for teachers of this course
    Available for teachers, students
    """
    serializer_class = homeworks_serializers.LectureDetailSerializer
    queryset = Homework.objects.all()
