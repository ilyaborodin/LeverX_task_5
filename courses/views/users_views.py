from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from djoser.serializers import UserSerializer
from courses.models import User
from courses.permissions.courses_permissions import IsTeacher


@permission_classes((IsAuthenticated, IsTeacher))
class StudentsListView(generics.ListAPIView):
    """
    Retrieve list of students
    List is needed to be able to get user id when adding it to course
    Available for teachers
    """
    queryset = User.objects.filter(user_type="Student")
    serializer_class = UserSerializer


@permission_classes((IsAuthenticated, IsTeacher))
class TeachersListView(generics.ListAPIView):
    """
    Retrieve list of teachers
    List is needed to be able to get user id when adding it to course
    Available for teachers
    """
    queryset = User.objects.filter(user_type="Teacher")
    serializer_class = UserSerializer
