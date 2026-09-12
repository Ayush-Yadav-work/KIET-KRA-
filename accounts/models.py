from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Department

class User(AbstractUser):
    ROLE_CHOICES = (
        ('SUPER_ADMIN', 'Super Admin'),
        ('HOD', 'Head of Department'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='HOD')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    def __str__(self):
        return f"{self.username} ({self.role})"
