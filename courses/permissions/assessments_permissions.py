from rest_framework import permissions
from courses.models import Solution
from courses.permissions.methods import check_teacher, check_participant
from django.core.exceptions import ObjectDoesNotExist


class IsParticipantObj(permissions.BasePermission):
    """
    Check is participant of assessment's course by object
    """
    message = "Only teacher or student with method save can access this API. " \
              "User must be a member of this course"

    def has_object_permission(self, request, view, obj):
        course = obj.solution.homework.lecture.course
        return check_participant(request, course)


class IsTeacherParticipant(permissions.BasePermission):
    """
    Check is participant of assessment's course by field
    """
    message = "Only teacher or student with method save can access this API. " \
              "User must be a member of this course"

    def has_permission(self, request, view):
        solution_id = request.data.get("solution")
        if solution_id is None:
            self.message = "Solution in request.data does not exist"
            return False
        try:
            solution = Solution.objects.get(id=solution_id)
        except ObjectDoesNotExist:
            self.message = "Solution does not exist"
            return False
        course = solution.homework.lecture.course
        return check_teacher(request, course)
