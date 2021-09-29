from rest_framework import serializers

from . import *
from ..models import Board
from users.serializers import UserSerializer
    
class BoardSerializer ( serializers.ModelSerializer ):
    model = Board

    folder = FolderSerializer()
    user = UserSerializer()
    shared_with = UserSerializer(many=True)

    class Meta:
        model = Board
        fields = '__all__'