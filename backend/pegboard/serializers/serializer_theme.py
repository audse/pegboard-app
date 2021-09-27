from rest_framework import serializers

from ..models import Theme

class ThemeSerializer ( serializers.ModelSerializer ):
    model = Theme
    class Meta:
        model = Theme
        fields = '__all__'
