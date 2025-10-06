# tourism_backend/tourism_backend/urls.py

from django.contrib import admin
from django.urls import path, include

# Import the Graphene view
from graphene_django.views import GraphQLView
# Import the schema we just created
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # -----------------------------------------------------------
    # API Endpoints (Single GraphQL endpoint)
    # -----------------------------------------------------------
    # The single entry point for all API queries and mutations
    # graphiql=True enables the in-browser IDE for testing (essential for development)
    path('api/graphql/', GraphQLView.as_view(graphiql=True, schema=schema), name='graphql'),
    
    # NOTE: Any previous path('api/auth/', include('apps.users.urls')) should be removed.
]