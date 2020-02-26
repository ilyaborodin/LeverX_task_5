from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import CourseDetailSerializer, CoursesListSerializer
from .models import Course
from .permissions import IsStudent, IsTeacher, IsOwnerOrReadOnly
from django.db.models import Q


@permission_classes((IsAuthenticated, IsTeacher))
class CourseCreateView(generics.CreateAPIView):
    """
    Create Course
    Available for teachers
    """
    serializer_class = CourseDetailSerializer


@permission_classes((IsAuthenticated, IsOwnerOrReadOnly))
class CoursesDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy course
    Available for all users
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
        return Course.objects.filter(author=user)


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
        return Course.objects.filter(Q(teachers=user) | Q(author=user))
