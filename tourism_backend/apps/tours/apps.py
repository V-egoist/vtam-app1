
# apps/tours/apps.py

from django.apps import AppConfig

class ToursConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tours' # <--- CRITICAL: Defines the full dotted path
    verbose_name = 'Tours and Locations' # <--- Optional, but helpful name