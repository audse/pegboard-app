from rest_framework import serializers

from . import *
from ..models import Folder

class FolderSerializer ( serializers.ModelSerializer ):

    model = Folder

    board = BoardSerializer(many=True)

    class Meta:
        model = Folder
        fields = '__all__'
