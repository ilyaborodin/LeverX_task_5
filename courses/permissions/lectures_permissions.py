from rest_framework import permissions
from courses.models import Course


class IsParticipantObj(permissions.BasePermission):
    """
    Check is participant of lecture's course by object
    """
    def has_object_permission(self, request, view, obj):
        course = obj.course
        return check_permission(request, course)


class IsParticipantID(permissions.BasePermission):
    """
    Check is participant of lecture's course by field course
    """
    def has_permission(self, request, view):
        course_id = request.data.get("course")
        course = Course.objects.get(id=course_id)
        return check_permission(request, course)


class IsParticipantPK(permissions.BasePermission):
    """
    Check is participant of lecture's course by pk
    """
    def has_permission(self, request, view):
        course_id = view.kwargs["pk"]
        course = Course.objects.get(id=course_id)
        return check_permission(request, course)


def check_permission(request, course):
    if request.user.user_type == "Student":
        if request.method not in permissions.SAFE_METHODS:
            return False
        return request.user in course.students.all()
    elif request.user.user_type == "Teacher":
        return request.user in course.teachers.all()