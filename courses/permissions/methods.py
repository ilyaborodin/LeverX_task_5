from rest_framework import permissions


def check_permission_for_teachers_privileges(request, course):
    if request.user.user_type == "Student":
        if request.method not in permissions.SAFE_METHODS:
            return False
        return request.user in course.students.all()
    elif request.user.user_type == "Teacher":
        return request.user in course.teachers.all()


def check_participant(request, course):
    if request.user.user_type == "Student":
        return request.user in course.students.all()
    elif request.user.user_type == "Teacher":
        return request.user in course.teachers.all()


def check_student(request, course):
    if request.user.user_type == "Student":
        return request.user in course.students.all()


def check_teacher(request, course):
    if request.user.user_type == "Teacher":
        return request.user in course.students.all()
