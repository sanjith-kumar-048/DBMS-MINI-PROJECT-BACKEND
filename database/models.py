from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

#for custom userprofile manage
from django.contrib.auth.models import BaseUserManager

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


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('User must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)

        #best practice to use (using=self.db)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create a new superuser with given details"""
        user = self.create_user(email, name, password)

        #automatically created by PermissionsMixin
        user.is_superuser = True

        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    #overwrite default username to use email, so that Admin portal will display email and password
    #instad of username and password
    #also mark email as required or mandatory field
    USERNAME_FIELD = 'email'

    #explicitly declare fields which are required
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of user"""
        return self.name

    def __str__(self):
        """return string representation of user"""
        return self.email
