from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    """
    Check is user student
    """
    message = "Only student can access this API"

    def has_permission(self, request, view):
        user_type = request.user.user_type
        return user_type == "Student"


class IsTeacher(permissions.BasePermission):
    """
    Check is user teacher
    """
    message = "Only teacher can access API"

    def has_permission(self, request, view):
        user_type = request.user.user_type
        return user_type == "Teacher"


class IsTeacherOrReadOnly(permissions.BasePermission):
    """
    Check is user teacher or method save
    """
    message = "Only teacher or student with method save can access this API. " \
              "User must be a member of this course"

    def has_object_permission(self, request, view, obj):
        if request.user in obj.students.all() and request.method in permissions.SAFE_METHODS:
            return True
        return request.user in obj.teachers.all() and request.user.user_type == "Teacher"


class IsTeacherOrStudent(permissions.BasePermission):
    """
    Check is user teacher or student
    """
    message = "Only Student and Teacher can access this API"

    def has_permission(self, request, view):
        return request.user.user_type == "Teacher" or "Student"


class IsCreator(permissions.BasePermission):
    """
    Check is user creator
    """
    message = "Only creator of course can access this API. "

    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator


class IsNotAuthenticated(permissions.BasePermission):
    """
    Allows access only to not authenticated users.
    """

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)
