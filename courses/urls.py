from django.urls import path, include
from .views import courses_views

# auth
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
# courses
urlpatterns += [
    path('courses/teachers/course/create', courses_views.CourseCreateView.as_view()),
    path('courses/teachers/all/', courses_views.TeachersAndAuthorsCoursesListView.as_view()),
    path('courses/teachers/author/', courses_views.AuthorsCoursesListView.as_view()),
    path('courses/teachers/teacher/', courses_views.TeachersCoursesListView.as_view()),
    path('courses/students/all/', courses_views.CoursesListView.as_view()),
    path('courses/students/course/detail/<int:pk>/', courses_views.StudentsCourseDetailView.as_view()),
    path('courses/teachers/course/detail/<int:pk>/', courses_views.TeachersCourseDetailView.as_view()),
]
