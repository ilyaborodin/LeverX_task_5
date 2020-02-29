from rest_framework import permissions
from courses.models import Comment
from courses.permissions.methods import check_participant


class IsParticipantId(permissions.BasePermission):
    """
    Check is participant of comment's course by field
    """
    message = "Only user of this course can access this API"

    def has_permission(self, request, view):
        assessment_id = request.data.get("solution")
        comment = Comment.objects.get(id=assessment_id)
        course = comment.solution.homework.lecture.course
        return check_participant(request, course)


class IsParticipantPk(permissions.BasePermission):
    """
    Check is participant of comment's course by pk
    """
    message = "Only user of this course can access this API"

    def has_permission(self, request, view):
        assessment_id = view.kwargs["assessment"]
        comment = Comment.objects.get(id=assessment_id)
        course = comment.solution.homework.lecture.course
        return check_participant(request, course)
