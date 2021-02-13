from django.contrib import admin
from .models import Dept,Course,Student
# Register your models here.
admin.site.register(Dept)
admin.site.register(Course)
admin.site.register(Student)