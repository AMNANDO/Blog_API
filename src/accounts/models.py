from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    ROLE_ADMIN = 'admin'
    ROLE_AUTHOR = 'author'
    ROLE_USER = 'user'

    ROLE_CHOICES = (
        (ROLE_ADMIN, 'Admin'),
        (ROLE_AUTHOR, 'Author'),
        (ROLE_USER, 'User'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_USER
    )

    bio = models.TextField(blank=True)
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True
    )

    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    def is_author(self):
        return self.role == self.ROLE_AUTHOR

    def __str__(self):
        return self.username
