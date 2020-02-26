from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import CourseDetailSerializer, CoursesListSerializer
from courses.models import Course
from courses.permissions import IsStudent, IsTeacher, IsOwner
from django.db.models import Q


@permission_classes((IsAuthenticated, IsTeacher))
class CourseCreateView(generics.CreateAPIView):
    """
    Create Course
    Available for teachers
    """
    serializer_class = CourseDetailSerializer


@permission_classes((IsAuthenticated, IsStudent))
class StudentsCourseDetailView(generics.RetrieveAPIView):
    """
    Retrieve course
    Available for all users
    """
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()


@permission_classes((IsAuthenticated, IsTeacher, IsOwner))
class TeachersCourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    class StudentsCoursesDetailView(generics.RetrieveAPIView):
        """
        Retrieve, update, destroy teacher's own course
        Available for teachers
        """
        serializer_class = CourseDetailSerializer
        queryset = Course.objects.all()


@permission_classes((IsAuthenticated, IsStudent))
class CoursesListView(generics.ListAPIView):
    """
    Return all courses
    Available for students
    """
    serializer_class = CoursesListSerializer
    queryset = Course.objects.all()


@permission_classes((IsAuthenticated, IsTeacher))
class AuthorsCoursesListView(generics.ListAPIView):
    """
    Return list of courses where user is creator
    Available for Teachers
    """
    serializer_class = CoursesListSerializer

    def get_queryset(self):
        user = self.request.user
        return Course.objects.filter(user=user)


@permission_classes((IsAuthenticated, IsTeacher))
class TeachersCoursesListView(generics.ListAPIView):
    """
    Return list of courses where user is teacher and isn't creator
    Available for Teachers
    """
    serializer_class = CoursesListSerializer

    def get_queryset(self):
        user = self.request.user
        return Course.objects.filter(teachers=user)


@permission_classes((IsAuthenticated, IsTeacher))
class TeachersAndAuthorsCoursesListView(generics.ListAPIView):
    """
    Return list of courses where user can be teacher or creator
    Available for Teachers
    """
    serializer_class = CoursesListSerializer

    def get_queryset(self):
        user = self.request.user
        return Course.objects.filter(Q(teachers=user) | Q(user=user))
