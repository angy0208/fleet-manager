from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'users'


class Role(models.Model):

    PERMISSION_CHOICES = [
        (0, 'No access'),
        (1, 'View only'),
        (2, 'Create and modify'),
    ]

    role_name = models.CharField(
        max_length=50,
        unique=True
    )

    vehicles = models.IntegerField(
        choices=PERMISSION_CHOICES,
        default=0
    )

    drivers = models.IntegerField(
        choices=PERMISSION_CHOICES,
        default=0
    )

    trips = models.IntegerField(
        choices=PERMISSION_CHOICES,
        default=0
    )

    maintenance = models.IntegerField(
        choices=PERMISSION_CHOICES,
        default=0
    )

    expenses = models.IntegerField(
        choices=PERMISSION_CHOICES,
        default=0
    )

    reports = models.IntegerField(
        choices=PERMISSION_CHOICES,
        default=0
    )

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.role_name


class UserRole(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'user_roles'
        unique_together = ('user', 'role')

    def __str__(self):
        return f"{self.user.username} - {self.role.role_name}"