from rest_framework import serializers

from .models import Card, List, Board

class CardSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Card
        fields = '__all__'

class ListSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = List
        fields = '__all__'
    
class BoardSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Board
        fields = '__all__'