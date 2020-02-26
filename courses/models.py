from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils import Choices


class User(AbstractUser):
    USER_TYPES = Choices("Student", "Teacher", "Admin")
    user_type = models.CharField(verbose_name="Type of user", blank=False,
                                 choices=USER_TYPES, max_length=10)
    email = models.EmailField(verbose_name='Email address', blank=False, unique=True)
    REQUIRED_FIELDS = ['email', 'user_type']

    def __str__(self):
        return self.username


# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#
#     def __str__(self):
#         return self.user.username


class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name="author")
    teachers = models.ManyToManyField(User, verbose_name="Teachers of this course", blank=True, related_name="teachers")
    title = models.CharField(verbose_name="Name", blank=False, max_length=20, unique=True)
    description = models.TextField(verbose_name="Description", blank=True, max_length=200)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    course = models.ForeignKey(Course, verbose_name="Course of this lecture",
                               blank=False, on_delete=models.CASCADE)
    topic = models.CharField(verbose_name="Topic", blank=False, max_length=20)
    file = models.FileField(verbose_name="File", upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.topic


class Homework(models.Model):
    lecture = models.OneToOneField(Lecture, verbose_name="Lecture",
                                   blank=False, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Topic", blank=False, max_length=20)
    task = models.TextField(verbose_name="Task", blank=False, max_length=400)

    def __str__(self):
        return self.title


class Solution(models.Model):
    homework = models.OneToOneField(Homework, verbose_name="Homework",
                                    blank=False, on_delete=models.CASCADE)
    user = models.OneToOneField(User, verbose_name="Author",
                                blank=False, on_delete=models.CASCADE)
    link = models.CharField(verbose_name="Link of solution", blank=False, max_length=80)

    def __str__(self):
        return "Solution of {}".format(self.homework)


class Assessment(models.Model):
    solution = models.OneToOneField(Solution, verbose_name="Solution",
                                    blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name="Rating", blank=False,
                                 validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return "Assessment of {}".format(self.solution)


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="Author of this comment",
                             blank=False, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, verbose_name="Assessment",
                                   blank=False, on_delete=models.CASCADE)
    comment = models.CharField(verbose_name="Text of comment", blank=False, max_length=200)

    def __str__(self):
        return "Comment of {}".format(self.user.username)
