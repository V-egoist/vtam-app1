# apps/tours/filters.py

import django_filters
from .models import Location

# Concept: This class tells Django-Filter exactly which model fields 
# can be used for filtering in our GraphQL query.
class LocationFilter(django_filters.FilterSet):
    # This filter allows the client to search by 'type' (e.g., HIST, MUSE).
    type = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Location
        fields = ['type']