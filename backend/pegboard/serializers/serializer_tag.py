from django.db.models.fields import IntegerField
from rest_framework import serializers

from . import *
from ..models import Tag, Board, Color

class TagSerializer ( serializers.ModelSerializer ):

    model = Tag

    id = serializers.IntegerField(required=False)
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all(), required=False, allow_null=True)
    color = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all(), required=False, allow_null=True)
    
    class Meta:
        model = Tag
        fields = '__all__'
        depth = 1
