from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import solutions_serializers
from courses.permissions.solutions_permissions import IsParticipantObj, IsStudentParticipant, IsStudent
from courses.models import Solution
from courses.views.methods import custom_list


@permission_classes((IsAuthenticated, IsStudentParticipant))
class SolutionCreateView(generics.CreateAPIView):
    serializer_class = solutions_serializers.SolutionCreateSerializer


@permission_classes((IsAuthenticated, IsParticipantObj))
class SolutionDetailView(generics.RetrieveAPIView):
    serializer_class = solutions_serializers.SolutionDetailSerializer
    queryset = Solution.objects.all()


@permission_classes((IsAuthenticated, IsStudent))
class SolutionListView(generics.ListAPIView):
    serializer_class = solutions_serializers.SolutionListSerializer

    def get_queryset(self, *args, **kwargs):
        return Solution.objects.filter(creator=kwargs["pk"])

    def list(self, request, *args, **kwargs):
        return custom_list(self, request, *args, **kwargs)
