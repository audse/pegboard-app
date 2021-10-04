from rest_framework import serializers

from . import *
from ..models import Page, Board

class PageSerializer ( serializers.ModelSerializer ):
    
    model = Page

    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all(), allow_null=True)

    notes = NoteSerializer(many=True, required=False)
    
    comments = CommentSerializer(many=True, required=False)
    checklists = ChecklistSerializer(many=True, required=False)

    class Meta:
        model = Page
        fields = '__all__'
        depth = 2