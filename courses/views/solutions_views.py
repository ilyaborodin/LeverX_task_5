from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import solutions_serializers
from courses.permissions.solutions_permissions import IsParticipantObj, IsStudentParticipant,\
    IsTeacherParticipantOrStudent
from courses.models import Solution
from courses.views.methods import custom_list


@permission_classes((IsAuthenticated, IsStudentParticipant))
class SolutionCreateView(generics.CreateAPIView):
    """
    Create solution
    Available for students of this course
    """
    serializer_class = solutions_serializers.SolutionCreateSerializer


@permission_classes((IsAuthenticated, IsParticipantObj))
class SolutionDetailView(generics.RetrieveAPIView):
    """
    Retrieve solution of this course
    Available for teachers, students
    """
    serializer_class = solutions_serializers.SolutionDetailSerializer
    queryset = Solution.objects.all()


@permission_classes((IsAuthenticated, IsTeacherParticipantOrStudent))
class SolutionListView(generics.ListAPIView):
    """
    Retrieve list of solutions
    Available for teachers of this course, students
    """
    serializer_class = solutions_serializers.SolutionListSerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.user.user_type == "Student":
            return Solution.objects.filter(creator=self.request.user.id)
        else:
            return Solution.objects.filter(homework=kwargs["homework"])

    def list(self, request, *args, **kwargs):
        return custom_list(self, request, *args, **kwargs)
