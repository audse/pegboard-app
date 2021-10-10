from rest_framework import serializers

from . import *
from ..models import Board, Folder, Theme

class BoardSerializer ( serializers.ModelSerializer ):

    model = Board

    folder = serializers.PrimaryKeyRelatedField(queryset=Folder.objects.all(), required=False, allow_null=True)
    
    pages = PageSerializer(many=True, required=False)
    notes = NoteSerializer(many=True, required=False)

    tags = TagSerializer(many=True, required=False)
    colors = ColorSerializer(many=True, required=False)
    comments = CommentSerializer(many=True, required=False)
    checklists = ChecklistSerializer(many=True, required=False)

    theme = serializers.PrimaryKeyRelatedField(queryset=Theme.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Board
        fields = '__all__'
        depth = 2