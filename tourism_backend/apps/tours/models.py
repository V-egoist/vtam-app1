# apps/tours/models.py

from django.db import models

class Location(models.Model):
    """Model representing a geographical point of interest."""

    LOCATION_TYPES = (
        ('HIST', 'Historical Site'),
        ('MUSE', 'Museum'),
        ('NATE', 'Natural Landmark'),
        ('VENU', 'Venue/Activity'),
        ('REST', 'Restaurant/Food'),
        ('OTHR', 'Other'),
    )

    name = models.CharField(max_length=150, unique=True, help_text="Location name.")
    description = models.TextField(help_text="Location description.")
    type = models.CharField(
        max_length=4,
        choices=LOCATION_TYPES,
        default='OTHR',
        help_text="Location category."
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6, help_text="Geographical latitude.")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, help_text="Geographical longitude.")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'