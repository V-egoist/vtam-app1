# apps/users/urls.py

from django.urls import path
from .views import RegistrationView

app_name = 'users'

urlpatterns = [
    # This maps the path 'register/' to the RegistrationView.
    # The final path will be /api/auth/register/
    path('register/', RegistrationView.as_view(), name='register'),
]