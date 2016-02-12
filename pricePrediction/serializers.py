from models import CarAd
from rest_framework import serializers


class CarAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAd
        fields = (
            'kw',
            'km',
            'year',
            'idFromSite'
        )
