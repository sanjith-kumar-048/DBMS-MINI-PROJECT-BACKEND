from django.db import models
from django.db.models.base import Model, ModelState
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Department(models.Model):
    dept_id = models.CharField(
        max_length=10, unique=True, primary_key=True, blank=False, null=False)
    dept_name = models.CharField(max_length=250, unique=True, blank=False, null=False)

    def __str__(self):
        return  f"{self.dept_name}"


class Student(models.Model):
    usn = models.CharField(max_length=10,unique=True, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=60, blank=False, null=False)
    sem = models.IntegerField(validators=[
        MaxValueValidator(8),
        MinValueValidator(1)
    ], blank=False, null=False)
    section = models.CharField(max_length=1, blank=False, null=False)
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=False, null=False)
    department = models.ForeignKey(Department, related_name='dept', on_delete=models.CASCADE)


class Subject(models.Model):
    subject_code = models.CharField(max_length=10, null=False, blank=False, primary_key=True, unique=True)
    subject_name = models.CharField(max_length=50, null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Teacher(models.Model):
    ssn = models.CharField(max_length=10, null=False,
                           blank=False, primary_key=True, unique=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=False, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, unique=True)