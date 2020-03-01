from rest_framework import permissions
from courses.models import Lecture
from courses.permissions.methods import check_permission_for_teachers_privileges
from django.core.exceptions import ObjectDoesNotExist


class IsParticipantObj(permissions.BasePermission):
    """
    Check is participant of homework's course by object
    """
    message = "Only teacher or student with method save can access this API. " \
              "User must be a member of this course"

    def has_object_permission(self, request, view, obj):
        course = obj.lecture.course
        return check_permission_for_teachers_privileges(request, course)


class IsParticipantID(permissions.BasePermission):
    """
    Check is participant of homework's course by field
    """
    message = "Only teacher or student with method save can access this API. " \
              "User must be a member of this course"

    def has_permission(self, request, view):
        lecture_id = request.data.get("lecture")
        if lecture_id is None:
            self.message = "Lecture in request.data does not exist"
            return False
        try:
            lecture = Lecture.objects.get(id=lecture_id)
        except ObjectDoesNotExist:
            self.message = "Lecture does not exist"
            return False
        course = lecture.course
        return check_permission_for_teachers_privileges(request, course)
