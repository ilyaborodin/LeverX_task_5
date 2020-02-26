from rest_framework import permissions


class IsStudent(permissions.BasePermission):

    message = "Only API Student can access APIs"

    student = "Student"

    def has_permission(self, request, view):
        try:
            user_type = request.user.user_type
        except AttributeError:
            self.message = "Permission denied, user_type '{}' does not exists".format(self.student)
            return False
        return user_type == self.student


class IsStudent(permissions.BasePermission):

    message = "Only API Teacher can access APIs"

    teacher = "Teacher"

    def has_permission(self, request, view):
        try:
            user_type = request.user.user_type
        except AttributeError:
            self.message = "Permission denied, user_type '{}' does not exists".format(self.teacher)
            return False
        return user_type == self.teacher
