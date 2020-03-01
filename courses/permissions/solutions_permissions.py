from rest_framework import permissions
from courses.models import Homework
from courses.permissions.methods import check_participant, check_teacher, check_student
from django.core.exceptions import ObjectDoesNotExist


class IsParticipantObj(permissions.BasePermission):
    """
    Check is participant of solution's course by object
    """
    message = "Only user of this course can access this API"

    def has_object_permission(self, request, view, obj):
        course = obj.homework.lecture.course
        return check_participant(request, course)


class IsStudentParticipant(permissions.BasePermission):
    """
    Check is participant of solution's course by field
    """
    message = "Only student of this course can access this API"

    def has_permission(self, request, view):
        if request.user.user_type == "Teacher":
            return False
        homework_id = request.data.get("homework")
        if homework_id is None:
            self.message = "Homework in request.data does not exist"
            return False
        try:
            homework = Homework.objects.get(id=homework_id)
        except ObjectDoesNotExist:
            self.message = "Homework does not exist"
            return False
        course = homework.lecture.course
        return check_student(request, course)


class IsTeacherParticipantOrStudent(permissions.BasePermission):
    """
    Check is participant of solution's course by field
    """
    message = "Only user of this course can access this API"

    def has_permission(self, request, view):
        if request.user.user_type == "Student":
            return True
        try:
            homework_id = view.kwargs["homework"]
        except KeyError:
            self.message = "Homework in url does not exist"
            return False
        try:
            homework = Homework.objects.get(id=homework_id)
        except ObjectDoesNotExist:
            self.message = "Homework does not exist"
            return False
        course = homework.lecture.course
        return check_teacher(request, course)
