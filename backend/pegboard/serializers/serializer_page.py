from rest_framework import serializers

from . import *
from ..models import Page, Board

class PageSerializer ( serializers.ModelSerializer ):
    
    model = Page

    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all(), required=False, allow_null=True)

    notes = NoteSerializer(many=True, required=False, read_only=True)
    
    comments = CommentSerializer(many=True, required=False, read_only=True)
    checklists = ChecklistSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Page
        fields = '__all__'
        depth = 2