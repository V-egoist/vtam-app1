# apps/users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# CRITICAL FIX: The model is named 'User' in models.py, so we must import 'User'.
from .models import User 

# Concept: The CustomUserAdmin class now correctly references the imported 'User' model.
class CustomUserAdmin(UserAdmin):
    # CRITICAL FIX: Change model = CustomUser to the correct model name.
    model = User 
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_tourist', 'is_guide', 'is_staff']
    
    # We keep the custom fieldsets which is correct for displaying your fields.
    # Keep default UserAdmin.fieldsets and add a small 'Roles' section. Do
    # NOT re-declare 'first_name' and 'last_name' here because they already
    # exist in the base UserAdmin.fieldsets which would cause a duplicate
    # field error (admin.E012).
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {'fields': ('is_tourist', 'is_guide')}),
    )

# CRITICAL FIX: Change the registered model name.
admin.site.register(User, CustomUserAdmin)