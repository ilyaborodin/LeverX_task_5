from rest_framework import permissions
from courses.models import Comment


class IsParticipantId(permissions.BasePermission):
    def has_permission(self, request, view):
        assessment_id = request.data.get("solution")
        comment = Comment.objects.get(id=assessment_id)
        course = comment.solution.homework.lecture.course
        if request.user.user_type == "Student":
            return request.user in course.students.all()
        elif request.user.user_type == "Teacher":
            return request.user in course.teachers.all()


class IsParticipantPk(permissions.BasePermission):
    def has_permission(self, request, view):
        assessment_id = view.kwargs["pk"]
        comment = Comment.objects.get(id=assessment_id)
        course = comment.solution.homework.lecture.course
        if request.user.user_type == "Student":
            return request.user in course.students.all()
        elif request.user.user_type == "Teacher":
            return request.user in course.teachers.all()
