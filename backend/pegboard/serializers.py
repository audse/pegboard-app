from rest_framework import serializers

from .models import Card, List, Board

class CardSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Card
        fields = ['list', 'board', 'name', 'content', 'display', 'url', 'order', 'date_due', 'date_todo', 'date_created', 'date_updated']

class ListSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = List
        fields = ['board', 'name', 'description', 'url', 'order', 'date_created']
    
class BoardSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Board
        fields = ['name', 'description', 'url', 'order', 'date_created']