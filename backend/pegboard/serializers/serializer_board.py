from rest_framework import serializers

from . import *
from ..models import Board
    
class BoardSerializer ( serializers.ModelSerializer ):

    model = Board
    
    pages = PageSerializer(many=True)

    comments = CommentSerializer(many=True)
    checklists = ChecklistSerializer(many=True)

    class Meta:
        model = Board
        fields = '__all__'
        depth = 2