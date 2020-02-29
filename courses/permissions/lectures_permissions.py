from rest_framework import permissions
from courses.models import Course
from courses.permissions.methods import check_permission_for_teachers_privileges


class IsParticipantObj(permissions.BasePermission):
    """
    Check is participant of lecture's course by object
    """
    message = "Only teacher or student with method save can access this API"

    def has_object_permission(self, request, view, obj):
        course = obj.course
        return check_permission_for_teachers_privileges(request, course)


class IsParticipantID(permissions.BasePermission):
    """
    Check is participant of lecture's course by field course
    """
    message = "Only teacher or student with method save can access this API"

    def has_permission(self, request, view):
        course_id = request.data.get("course")
        course = Course.objects.get(id=course_id)
        return check_permission_for_teachers_privileges(request, course)


class IsParticipantPK(permissions.BasePermission):
    """
    Check is participant of lecture's course by pk
    """
    message = "Only teacher or student with method save can access this API"

    def has_permission(self, request, view):
        course_id = view.kwargs["course_id"]
        course = Course.objects.get(id=course_id)
        return check_permission_for_teachers_privileges(request, course)
