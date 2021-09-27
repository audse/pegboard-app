from rest_framework import serializers

from ..models import Folder

class FolderSerializer ( serializers.ModelSerializer ):
    model = Folder
    class Meta:
        model = Folder
        fields = '__all__'
