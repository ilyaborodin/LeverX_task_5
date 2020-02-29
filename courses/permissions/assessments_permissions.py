from rest_framework import permissions
from courses.models import Solution
from courses.permissions.methods import check_teacher, check_participant


class IsParticipantObj(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        course = obj.solution.homework.lecture.course
        return check_participant(request, course)


class IsTeacherParticipant(permissions.BasePermission):
    def has_permission(self, request, view):
        solution_id = request.data.get("solution")
        solution = Solution.objects.get(id=solution_id)
        course = solution.homework.lecture.course
        return check_teacher(request, course)
