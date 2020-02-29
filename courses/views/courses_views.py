from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import courses_serializers
from courses.models import Course
from courses.permissions.courses_permissions import IsTeacher, IsTeacherOrReadOnly, IsTeacherOrStudent


@permission_classes((IsAuthenticated, IsTeacher))
class CourseCreateView(generics.CreateAPIView):
    """
    Create Course
    Available for teachers
    """
    serializer_class = courses_serializers.CreatorCourseDetailSerializer


@permission_classes((IsAuthenticated, IsTeacherOrReadOnly))
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get course for students
    Retrieve/Update/Destroy course for creator
    Retrieve available course, update students field for teachers
    Available for all teachers, students
    """
    serializer_class = courses_serializers.CourseDetailSerializer
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.request.user == self.get_object().creator:
            serializer = courses_serializers.CreatorCourseDetailSerializer
        else:
            serializer = courses_serializers.CourseDetailSerializer
        return serializer


@permission_classes((IsAuthenticated, IsTeacherOrStudent))
class CoursesListView(generics.ListAPIView):
    """
    Retrieve all courses for students
    Retrieve all available courses for teachers
    Available for all teachers, students
    """
    serializer_class = courses_serializers.CoursesListSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == "Teacher":
            queryset = Course.objects.filter(teachers=user)
        else:
            queryset = Course.objects.filter(students=user)
        return queryset


@permission_classes((IsAuthenticated, IsTeacher))
class AuthorsCoursesListView(generics.ListAPIView):
    """
    Retrieve courses where user is creator
    Available for Teachers
    """
    serializer_class = courses_serializers.CoursesListSerializer

    def get_queryset(self):
        user = self.request.user
        return Course.objects.filter(creator=user)
