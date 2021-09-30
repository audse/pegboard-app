from rest_framework import serializers

from . import *
from ..models import Board
from users.serializers import UserSerializer
    
class BoardSerializer ( serializers.ModelSerializer ):
    model = Board

    class Meta:
        model = Board
        fields = '__all__'
        depth = 2