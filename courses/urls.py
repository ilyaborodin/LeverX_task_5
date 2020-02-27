from django.urls import path, include
from .views import courses_views

# auth
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

# courses
urlpatterns += [
    path('courses/course/create', courses_views.CourseCreateView.as_view()),
    path('courses/all/', courses_views.CoursesListView.as_view()),
    path('courses/all/author/', courses_views.AuthorsCoursesListView.as_view()),
    path('courses/course/detail/<int:pk>/', courses_views.CourseDetailView.as_view()),
]
