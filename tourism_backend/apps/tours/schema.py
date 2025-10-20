# apps/tours/schema.py

import graphene
from graphene_django import DjangoObjectType, DjangoConnectionField
from django.db.models.functions import Cos, Radians, Sin, ACos
from django.db.models import F, FloatField, ExpressionWrapper
from .models import Location
from .filters import LocationFilter

# 1. Location Type Definition
class LocationType(DjangoObjectType):
    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'type', 'latitude', 'longitude', 'created_at', 'updated_at')
        interfaces = (graphene.relay.Node,)


# 2. Location Query Definition
class LocationQuery(graphene.ObjectType):

    # ✅ Only Graphene fields here (NO filterset_class)
    all_locations = DjangoConnectionField(
        LocationType,
        lat=graphene.Float(description="User's current latitude."),
        lng=graphene.Float(description="User's current longitude."),
        radius=graphene.Int(description="Search radius in kilometers (km)."),
        type=graphene.String(description="Filter by location type")  # Example: 'museum', 'hotel'
    )

    # Single location by ID
    location = graphene.Field(
        LocationType,
        id=graphene.Int(required=True)
    )

    # Resolver for single location
    def resolve_location(root, info, id):
        try:
            return Location.objects.get(pk=id)
        except Location.DoesNotExist:
            return None

    # ✅ Resolver for all locations with filtering & geo-distance
    def resolve_all_locations(root, info, **kwargs):
        queryset = Location.objects.all()

        # Apply filterset manually (for 'type' or other fields)
        filterset = LocationFilter(
            data=kwargs,
            queryset=queryset,
            request=getattr(info.context, 'request', None)
        )
        queryset = filterset.qs  # Filtered queryset

        # Geo-distance filtering
        lat = kwargs.get('lat')
        lng = kwargs.get('lng')
        radius = kwargs.get('radius')

        if lat is not None and lng is not None and radius is not None:
            R = 6371  # Earth's radius in km

            # Calculate distance using Haversine formula and ExpressionWrapper
            distance_calc = ExpressionWrapper(
                R * ACos(
                    Cos(Radians(lat)) * Cos(Radians(F('latitude'))) *
                    Cos(Radians(F('longitude')) - Radians(lng)) +
                    Sin(Radians(lat)) * Sin(Radians(F('latitude')))
                ),
                output_field=FloatField()  # ✅ This avoids the 'Cannot infer type' error
            )

            queryset = queryset.annotate(distance=distance_calc)
            queryset = queryset.filter(distance__lte=radius).order_by('distance')

        return queryset
