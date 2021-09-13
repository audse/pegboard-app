from rest_framework import serializers

from .models import Card, List, Board, Theme

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

class ThemeSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Theme
        fields = '__all__'