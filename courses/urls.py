from django.urls import path, include
from .views import courses_views, lectures_views

# auth
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

# courses
urlpatterns += [
    path('courses/course/create/', courses_views.CourseCreateView.as_view()),
    path('courses/all/', courses_views.CoursesListView.as_view()),
    path('courses/all/author/', courses_views.AuthorsCoursesListView.as_view()),
    path('courses/course/detail/<int:pk>/', courses_views.CourseDetailView.as_view()),
]

# lectures
urlpatterns += [
    path('lectures/lecture/create/', lectures_views.LectureCreateView.as_view()),
    path('lectures/lecture/<int:pk>/', lectures_views.LectureDetailView.as_view()),
    path('lectures/all/course/<int:pk>/', lectures_views.LecturesListView.as_view()),
]
