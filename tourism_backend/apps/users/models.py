# apps/users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model extending AbstractUser.
    Adds boolean fields to differentiate between Tourists and Guides.
    """
    # Inherits fields like username, password, email, first_name, etc.

    is_tourist = models.BooleanField(
        default=True,
        help_text='Designates whether this user is a tourist (default role).'
    )
    is_guide = models.BooleanField(
        default=False,
        help_text='Designates whether this user is a certified guide.'
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        # A simple, human-readable identifier for the user
        return self.username