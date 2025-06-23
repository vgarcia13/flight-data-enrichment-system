from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.HyperlinkedModelSerializer):
    flight_numbers = serializers.ListField(child=serializers.CharField(), default=list)
    legs = serializers.ListField(child=serializers.DictField(), default=list)

    class Meta:
        model = Flight
        fields = [
            'url',
            'id',
            'travel_class',
            'origin',
            'destination',
            'departure_time',
            'arrival_time',
            'flight_numbers',
            'legs',
            'last_seen'
        ]