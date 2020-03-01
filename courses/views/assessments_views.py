from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import assessments_serializers
from courses.permissions.assessments_permissions import IsParticipantObj, IsTeacherParticipant
from courses.models import Assessment


@permission_classes((IsAuthenticated, IsTeacherParticipant))
class AssessmentCreateView(generics.CreateAPIView):
    """
    Create assessment
    Available for teachers of this course
    """
    serializer_class = assessments_serializers.AssessmentCreateSerializer


@permission_classes((IsAuthenticated, IsParticipantObj))
class AssessmentDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieve assessment of this course
    Available for teachers, students
    """
    serializer_class = assessments_serializers.AssessmentDetailSerializer
    queryset = Assessment.objects.all()
