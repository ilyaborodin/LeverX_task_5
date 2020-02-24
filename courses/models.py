from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils import Choices


class User(AbstractUser):
    USER_TYPES = Choices("Student", "Teacher")
    user_type = models.CharField(verbose_name="Type of user", blank=False,
                                 choices=USER_TYPES, max_length=10)
    email = models.EmailField(verbose_name='Email address', blank=False)

    def is_teacher(self):
        return self.user_type == self.USER_TYPES.Teacher

    def is_student(self):
        return self.user_type == self.USER_TYPES.Student
    REQUIRED_FIELDS = ['email', 'user_type']


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Course(models.Model):
    teacher = models.ManyToManyField(Teacher, verbose_name="Teachers of this course", blank=True)
    name = models.CharField(verbose_name="Name", blank=False, max_length=20)
    description = models.TextField(verbose_name="Description", blank=True, max_length=200)


class Lecture(models.Model):
    course = models.ForeignKey(Course, verbose_name="Course of this lecture",
                               blank=False, on_delete=models.CASCADE)
    topic = models.CharField(verbose_name="Topic", blank=False, max_length=20)
    file = models.FileField(verbose_name="File", upload_to='uploads/%Y/%m/%d/')


class Homework(models.Model):
    lecture = models.OneToOneField(Lecture, verbose_name="Lecture",
                                   blank=False, on_delete=models.CASCADE)
    task = models.CharField(verbose_name="Task", blank=False, max_length=400)


class Solution(models.Model):
    homework = models.OneToOneField(Homework, verbose_name="Homework",
                                    blank=False, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, verbose_name="Author",
                                   blank=False, on_delete=models.CASCADE)
    link = models.CharField(verbose_name="Link of solution", blank=False, max_length=80)


class Assessment(models.Model):
    solution = models.OneToOneField(Solution, verbose_name="Solution",
                                    blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name="Rating", blank=False,
                                 validators=[MinValueValidator(0), MaxValueValidator(100)])


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="Author of this comment",
                             blank=False, on_delete=models.CASCADE)
    comment = models.CharField(verbose_name="Text of comment", blank=False, max_length=200)
