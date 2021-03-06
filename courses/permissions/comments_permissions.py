from rest_framework import permissions
from courses.models import Comment, Assessment
from courses.permissions.methods import check_participant
from django.core.exceptions import ObjectDoesNotExist


class IsParticipantId(permissions.BasePermission):
    """
    Check is participant of comment's course by field
    """
    message = "Only teacher or student with method save can access this API. " \
              "User must be a member of this course"

    def has_permission(self, request, view):
        assessment_id = request.data.get("assessment")
        if assessment_id is None:
            self.message = "Assessment in request.data does not exist"
            return False
        try:
            assessment = Assessment.objects.get(id=assessment_id)
        except ObjectDoesNotExist:
            self.message = "Assessment does not exist"
            return False
        course = assessment.solution.homework.lecture.course
        return check_participant(request, course)


class IsParticipantPk(permissions.BasePermission):
    """
    Check is participant of comment's course by pk
    """
    message = "Only teacher or student with method save can access this API. " \
              "User must be a member of this course"

    def has_permission(self, request, view):
        try:
            assessment_id = view.kwargs["assessment_id"]
        except KeyError:
            self.message = "Assessment in url does not exist"
            return False
        try:
            assessment = Assessment.objects.get(id=assessment_id)
        except ObjectDoesNotExist:
            self.message = "Assessment does not exist"
            return False
        course = assessment.solution.homework.lecture.course
        return check_participant(request, course)
