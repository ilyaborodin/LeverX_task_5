from rest_framework import permissions
from courses.models import Solution


class IsParticipantObj(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        course = obj.solution.homework.lecture.course
        if request.user.user_type == "Student":
            return request.user in course.students.all()
        elif request.user.user_type == "Teacher":
            return request.user in course.teachers.all()


class IsTeacherParticipant(permissions.BasePermission):
    def has_permission(self, request, view):
        solution_id = request.data.get("solution")
        solution = Solution.objects.get(id=solution_id)
        course = solution.homework.lecture.course
        if request.user.user_type == "Teacher":
            return request.user in course.teachers.all()
