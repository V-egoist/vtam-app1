# apps/users/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer

class RegistrationView(APIView):
    """
    Handles user registration via POST request.
    Creates a new User object if data is valid.
    """
    def post(self, request):
        # 1. Initialize the serializer with the request data
        serializer = UserRegistrationSerializer(data=request.data)
        
        # 2. Check if the data is valid (e.g., username not taken, required fields present)
        if serializer.is_valid():
            # 3. Save the new user (triggers the create() method in the serializer)
            user = serializer.save()

            # 4. Return success response (HTTP 201 Created)
            # serializer.data contains the new user info (minus the password)
            return Response({
                "message": "User registered successfully.",
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        # 5. Return detailed error response (HTTP 400 Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)