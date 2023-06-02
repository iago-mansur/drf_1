from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):

    class meta:
        model = Drink
        fields = ['id', 'name', 'description']