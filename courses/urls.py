from django.urls import path, include
from courses.views import courses_views, lectures_views, homeworks_views,\
    solutions_views, assessments_views, comments_views

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
    path('lectures/all/course/<int:course>/', lectures_views.LecturesListView.as_view()),
]

# homework
urlpatterns += [
    path('homework/create/', homeworks_views.LectureCreateView.as_view()),
    path('homework/<int:pk>/', homeworks_views.LectureDetailView.as_view()),
]

# solutions
urlpatterns += [
    path('solutions/solution/create/', solutions_views.SolutionCreateView.as_view()),
    path('solutions/solution/<int:pk>/', solutions_views.SolutionDetailView.as_view()),
    path('solutions/all/', solutions_views.SolutionListView.as_view()),
]

# assessments
urlpatterns += [
    path('assessments/assessment/create/', assessments_views.AssessmentCreateView),
    path('assessments/assessment/<int:pk>/', assessments_views.AssessmentDetailView),
]

# comments
urlpatterns += [
    path('comments/comment/create/', comments_views.CommentCreateView.as_view()),
    path('comments/all/<int:assessment>/', comments_views.CommentListView.as_view()),
    path('comments/all/', comments_views.CommentListView.as_view()),
]
