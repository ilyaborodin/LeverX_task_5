from rest_framework import permissions
from courses.models import Course
from courses.permissions.methods import check_permission_for_teachers_privileges
from django.core.exceptions import ObjectDoesNotExist


class IsParticipantObj(permissions.BasePermission):
    """
    Check is participant of lecture's course by object
    """
    message = "Only teacher or student with method save can access this API. " \
              "User must be a member of this course"

    def has_object_permission(self, request, view, obj):
        course = obj.course
        return check_permission_for_teachers_privileges(request, course)


class IsParticipantID(permissions.BasePermission):
    """
    Check is participant of lecture's course by field course
    """
    message = "Only teacher or student with method save can access this API. " \
              "User must be a member of this course"

    def has_permission(self, request, view):
        course_id = request.data.get("course")
        if course_id is None:
            self.message = "Course in request.data does not exist"
            return False
        try:
            course = Course.objects.get(id=course_id)
        except ObjectDoesNotExist:
            self.message = "Course does not exist"
            return False
        return check_permission_for_teachers_privileges(request, course)


class IsParticipantPK(permissions.BasePermission):
    """
    Check is participant of lecture's course by pk
    """
    message = "Only teacher or student with method save can access this API. " \
              "User must be a member of this course"

    def has_permission(self, request, view):
        try:
            course_id = view.kwargs["course_id"]
        except KeyError:
            self.message = "Course in url does not exist"
            return False
        try:
            course = Course.objects.get(id=course_id)
        except ObjectDoesNotExist:
            self.message = "Course does not exist"
            return False
        return check_permission_for_teachers_privileges(request, course)
