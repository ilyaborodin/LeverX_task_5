from django.urls import path, include
from .views import CourseCreateView, CoursesListView

# auth
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
# courses
urlpatterns += [
    path('teacher/courses/course/create', CourseCreateView.as_view()),
    path('student/courses/all/', CoursesListView.as_view()),
]
