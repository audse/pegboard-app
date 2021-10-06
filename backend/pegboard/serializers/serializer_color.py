from rest_framework import serializers

from ..models import Color, Board

class ColorSerializer ( serializers.ModelSerializer ):
    model = Color

    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Color
        fields = '__all__'
