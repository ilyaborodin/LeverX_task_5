from rest_framework import permissions
from courses.models import Homework


class IsParticipantObj(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        course = obj.homework.lecture.course
        if request.user.user_type == "Student":
            return request.user in course.students.all()
        elif request.user.user_type == "Teacher":
            return request.user in course.teachers.all()


class IsStudentParticipant(permissions.BasePermission):
    def has_permission(self, request, view):
        homework_id = request.data.get("homework")
        homework = Homework.objects.get(id=homework_id)
        course = homework.lecture.course
        if request.user.user_type == "Student":
            return request.user in course.students.all()
