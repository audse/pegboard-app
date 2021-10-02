from rest_framework import serializers

from . import *
from ..models import Folder

class FolderSerializer ( serializers.ModelSerializer ):

    model = Folder

    boards = BoardSerializer(many=True, required=False)

    class Meta:
        model = Folder
        fields = '__all__'
