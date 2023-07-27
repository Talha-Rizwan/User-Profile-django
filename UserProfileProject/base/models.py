from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=150,unique=False, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True
    )
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    UNVERIFIED = 'Unverified'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (UNVERIFIED, 'Unverified'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=UNVERIFIED,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
