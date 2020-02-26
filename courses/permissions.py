from rest_framework import permissions


class IsStudent(permissions.BasePermission):

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

    message = "Only Teacher can access API"

    teacher = "Teacher"

    def has_permission(self, request, view):
        try:
            user_type = request.user.user_type
        except AttributeError:
            self.message = "Permission denied, user_type '{}' does not exists".format(self.teacher)
            return False
        return user_type == self.teacher


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
