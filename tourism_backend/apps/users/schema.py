# apps/users/schema.py

import graphene
from graphql_jwt.decorators import login_required
from .models import User
from .serializers import UserRegistrationSerializer # We still use the serializer for validation

# -----------------------------------------------------------
# 1. User Type (Defines the structure of a User returned by GraphQL)
# -----------------------------------------------------------
class UserType(graphene.ObjectType):
    """
    Defines which User model fields are exposed to the GraphQL API.
    """
    id = graphene.Int()
    username = graphene.String()
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    is_tourist = graphene.Boolean()
    is_guide = graphene.Boolean()
    # Note: We never expose the password field here

# -----------------------------------------------------------
# 2. Register Mutation (Handles user sign-up logic)
# -----------------------------------------------------------
class RegisterUser(graphene.Mutation):
    """
    GraphQL Mutation for creating a new user (Registration).
    """
    # Define what the mutation returns on success
    user = graphene.Field(UserType)
    message = graphene.String()

    # Define the required input fields
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        is_tourist = graphene.Boolean(required=True)
        is_guide = graphene.Boolean(required=True)

    def mutate(root, info, **kwargs):
        """
        The method that handles the business logic (creating the user).
        """
        # We reuse our existing REST serializer for validation and the secure create() method
        serializer = UserRegistrationSerializer(data=kwargs)
        
        if serializer.is_valid():
            # serializer.save() calls our create() method with hashed password
            user = serializer.save()
            
            return RegisterUser(
                user=user, 
                message="User registered successfully."
            )
        
        # If invalid, raise an error with the serializer details
        # In GraphQL, errors are often returned in a specific 'errors' field or raised.
        # For simplicity, we return a null user and the error message.
        error_messages = ", ".join([f"{k}: {v[0]}" for k, v in serializer.errors.items()])
        
        return RegisterUser(
            user=None,
            message=f"Validation failed: {error_messages}"
        )

# -----------------------------------------------------------
# 3. Users App Root Mutation
# -----------------------------------------------------------
class UserMutation(graphene.ObjectType):
    """
    Combines all mutations related to the Users app.
    """
    register_user = RegisterUser.Field()

# -----------------------------------------------------------
# 4. Users App Root Query (For fetching data)
# -----------------------------------------------------------
class UserQuery(graphene.ObjectType):
    # A simple query to test if a user is logged in
    me = graphene.Field(UserType)

    @login_required
    def resolve_me(root, info):
        # The login_required decorator ensures info.context.user exists and is authenticated
        return info.context.user