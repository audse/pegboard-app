from rest_framework import serializers

from ..models import Color

class ColorSerializer ( serializers.ModelSerializer ):
    model = Color
    class Meta:
        model = Color
        fields = '__all__'
