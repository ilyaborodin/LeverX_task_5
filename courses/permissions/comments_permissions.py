from rest_framework import permissions
from courses.models import Comment
from courses.permissions.methods import check_participant


class IsParticipantId(permissions.BasePermission):
    def has_permission(self, request, view):
        assessment_id = request.data.get("solution")
        comment = Comment.objects.get(id=assessment_id)
        course = comment.solution.homework.lecture.course
        return check_participant(request, course)


class IsParticipantPk(permissions.BasePermission):
    def has_permission(self, request, view):
        assessment_id = view.kwargs["pk"]
        comment = Comment.objects.get(id=assessment_id)
        course = comment.solution.homework.lecture.course
        return check_participant(request, course)
