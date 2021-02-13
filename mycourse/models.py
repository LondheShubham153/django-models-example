from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dept(models.Model):
    dept_id = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    course_id = models.CharField(primary_key='True', max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dept_id = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)
    prn = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)
    DOB = models.DateField(default='1998-01-01')

    def __str__(self):
        return self.name