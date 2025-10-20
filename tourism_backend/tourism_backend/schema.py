# tourism_backend/tourism_backend/schema.py

import graphene
import graphql_jwt

# Import users app schema
from apps.users import schema as users_schema 
from apps.tours import schema as tours_schema # <--- ADD THIS IMPORT

# -----------------------------------------------------------
# Root Query
# -----------------------------------------------------------
class Query(
    users_schema.UserQuery, 
    tours_schema.LocationQuery, # <--- ADD THIS INHERITANCE
    graphene.ObjectType
):
    hello = graphene.String(default_value="Hello Valentino! Your GraphQL API is running.")

# -----------------------------------------------------------
# Root Mutation
# -----------------------------------------------------------
class Mutation(users_schema.UserMutation, graphene.ObjectType):
    # 1. Login (Simplified to only provide Access Token for stability)
    token_auth = graphql_jwt.ObtainJSONWebToken.Field() 

    # 2. Security Check (Verification is the only essential JWT utility to keep)
    verify_token = graphql_jwt.Verify.Field()

# -----------------------------------------------------------
# Final GraphQL schema
# -----------------------------------------------------------
schema = graphene.Schema(query=Query, mutation=Mutation)