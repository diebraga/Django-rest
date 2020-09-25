from rest_framework import serializers
from .models import Car_dealers

class Car_dealersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_dealers
        fields = '__all__'
