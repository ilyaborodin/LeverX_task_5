from rest_framework import permissions
from courses.models import Course, Lecture
from courses.permissions.lectures_permissions import check_permission


class IsParticipantObj(permissions.BasePermission):
    """
    Check is participant of homework's course by object
    """
    def has_object_permission(self, request, view, obj):
        course = obj.lecture.course
        return check_permission(request, course)


class IsParticipantID(permissions.BasePermission):
    """
    Check is participant of homework's course by field course
    """
    def has_permission(self, request, view):
        lecture_id = request.data.get("lecture")
        lecture = Lecture.objects.get(id=lecture_id)
        course = Course.objects.get(id=lecture.id)
        return check_permission(request, course)
