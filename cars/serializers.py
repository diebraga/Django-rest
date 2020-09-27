from rest_framework import serializers
from .models import Cars

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('title', 'year', 'city', 'state', 'price', 'sale_type', 'new', 'photo_main')

class CarsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'
        lookup_field = 'id'

        
