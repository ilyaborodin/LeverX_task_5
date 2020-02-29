from rest_framework import permissions
from courses.models import Homework
from courses.permissions.courses_permissions import IsStudent
from courses.permissions.methods import check_participant, check_student


class IsParticipantObj(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        course = obj.homework.lecture.course
        return check_participant(request, course)


class IsStudentParticipant(permissions.BasePermission):
    def has_permission(self, request, view):
        homework_id = request.data.get("homework")
        homework = Homework.objects.get(id=homework_id)
        course = homework.lecture.course
        return check_student(request, course)
