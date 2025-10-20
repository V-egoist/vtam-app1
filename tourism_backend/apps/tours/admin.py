# apps/tours/admin.py

from django.contrib import admin
from .models import Location

# Concept: The admin.site.register() function tells the Django Admin 
# to create the necessary forms and links to manage the Location model data.
admin.site.register(Location)