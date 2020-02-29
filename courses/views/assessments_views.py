from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import assessments_serializers
from courses.permissions.assessments_permissions import IsParticipantObj, IsTeacherParticipant
from courses.models import Assessment


@permission_classes((IsAuthenticated, IsTeacherParticipant))
class AssessmentCreateView(generics.CreateAPIView):
    serializer_class = assessments_serializers.AssessmentCreateSerializer


@permission_classes((IsAuthenticated, IsParticipantObj))
class AssessmentDetailView(generics.RetrieveAPIView):
    serializer_class = assessments_serializers.AssessmentDetailSerializer
    queryset = Assessment.objects.all()

