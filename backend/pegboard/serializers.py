from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Card, List, Board, Theme

class ProfileSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = '__all__'

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