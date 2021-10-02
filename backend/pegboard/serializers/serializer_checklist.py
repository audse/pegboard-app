from rest_framework import serializers
import json

from ..models import Checklist, Board, Page, Note

class ChecklistSerializer ( serializers.ModelSerializer ):
    model = Checklist

    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all(), allow_null=True)
    page = serializers.PrimaryKeyRelatedField(queryset=Page.objects.all(), allow_null=True)
    note = serializers.PrimaryKeyRelatedField(queryset=Note.objects.all(), allow_null=True)

    class Meta:
        model = Checklist
        fields = '__all__'
        depth = 1