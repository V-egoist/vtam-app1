# tourism_backend/tourism_backend/schema.py

import graphene
import graphql_jwt
# 1. Ensure you have the correct import for your users app schema
from apps.users import schema as users_schema 

# -----------------------------------------------------------
# 2. Root Query (MUST be defined before the Mutation class)
# -----------------------------------------------------------
# Inherit all query fields from users_schema.UserQuery
class Query(users_schema.UserQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hello Valentino! Your GraphQL API is running.")

# -----------------------------------------------------------
# 3. Root Mutation
# -----------------------------------------------------------
# Inherit all mutation fields from users_schema.UserMutation
class Mutation(users_schema.UserMutation, graphene.ObjectType):
    # --- JWT Authentication Mutations ---
    token_auth = graphql_jwt.ObtainJSONWebToken.Field() 
    verify_token = graphql_jwt.Verify.Field()      
    refresh_token = graphql_jwt.Refresh.Field()    

# -----------------------------------------------------------
# 4. Final Schema Object
# -----------------------------------------------------------
schema = graphene.Schema(query=Query, mutation=Mutation)