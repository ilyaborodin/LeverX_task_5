from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import courses_serializers
from courses.models import Course
from courses.permissions.courses_permissions import IsTeacher, IsTeacherOrReadOnly, IsTeacherOrStudent, IsCreator


@permission_classes((IsAuthenticated, IsTeacher))
class CourseCreateView(generics.CreateAPIView):
    """
    Create Course
    Available for teachers
    """
    serializer_class = courses_serializers.CreatorCourseDetailSerializer


@permission_classes((IsAuthenticated, IsTeacherOrReadOnly))
class CourseDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieve available course for students
    Retrieve available course, update students field for teachers
    Available for teachers, students
    """
    serializer_class = courses_serializers.CourseDetailSerializer
    queryset = Course.objects.all()


@permission_classes((IsAuthenticated, IsCreator))
class CourseCreatorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/Update/Destroy
    Available for creator
    """
    serializer_class = courses_serializers.CreatorCourseDetailSerializer
    queryset = Course.objects.all()


@permission_classes((IsAuthenticated, IsTeacherOrStudent))
class CoursesListView(generics.ListAPIView):
    """
    Retrieve all available courses for students
    Retrieve all available courses for teachers
    Available for teachers, students
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
