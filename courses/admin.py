from django.contrib import admin
from .models import User, Course, Lecture, Homework, Solution, Assessment, Comment

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Homework)
admin.site.register(Solution)
admin.site.register(Assessment)
admin.site.register(Comment)
