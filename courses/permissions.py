from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    """
    Check is user student
    """
    message = "Only Student can access this API"

    student = "Student"

    def has_permission(self, request, view):
        try:
            user_type = request.user.user_type
        except AttributeError:
            self.message = "Permission denied, user_type '{}' does not exists".format(self.student)
            return False
        return user_type == self.student


class IsTeacher(permissions.BasePermission):
    """
    Check is user teacher
    """
    message = "Only Teacher can access API"

    teacher = "Teacher"

    def has_permission(self, request, view):
        try:
            user_type = request.user.user_type
        except AttributeError:
            self.message = "Permission denied, user_type '{}' does not exists".format(self.teacher)
            return False
        return user_type == self.teacher


class IsTeacherOrReadOnly(permissions.BasePermission):
    """
    Check is user teacher or method save
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creator.user_type == request.user.user_type == "Teacher"


class IsTeacherOrStudent(permissions.BasePermission):
    """
    Check is user teacher or student
    """
    def has_permission(self, request, view):
        return request.user.user_type == "Teacher" or "Student"
