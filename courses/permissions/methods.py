from rest_framework import permissions


def check_permission_for_teachers_privileges(request, course):
    """
    Check is request.user is teacher or student with method save of this course
    """
    if request.user.user_type == "Student":
        if request.method not in permissions.SAFE_METHODS:
            return False
        return request.user in course.students.all()
    elif request.user.user_type == "Teacher":
        return request.user in course.teachers.all()


def check_participant(request, course):
    """
    Check is request.user is teacher or student of this course
    """
    if request.user.user_type == "Student":
        return request.user in course.students.all()
    elif request.user.user_type == "Teacher":
        return request.user in course.teachers.all()


def check_student(request, course):
    """
    Check is request.user is student of this course
    """
    if request.user.user_type == "Student":
        return request.user in course.students.all()


def check_teacher(request, course):
    """
    Check is request.user is teacher of this course
    """
    if request.user.user_type == "Teacher":
        return request.user in course.teachers.all()
