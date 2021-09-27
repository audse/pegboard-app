from rest_framework import serializers

from ..models import Board
    
class BoardSerializer ( serializers.ModelSerializer ):
    model = Board
    class Meta:
        model = Board
        fields = '__all__'