
from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Explicitly define the password field for input validation.
    # write_only=True means it's required for POST/PUT but not included in the GET response.
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )
    
    class Meta:
        model = User
        # List all fields the user can submit during registration
        fields = (
            'id', 
            'username', 
            'email', 
            'password', 
            'first_name', 
            'last_name', 
            'is_tourist', 
            'is_guide'
        )
        read_only_fields = ('id',) 

    def create(self, validated_data):
        """
        Custom logic to use the User manager's create_user method for secure hashing.
        """
        # 1. Pop the plaintext password
        password = validated_data.pop('password')
        
        # 2. Use create_user to hash the password and save the user object
        user = User.objects.create_user(
            password=password,
            **validated_data  # Pass the remaining validated fields
        )
        
        return user