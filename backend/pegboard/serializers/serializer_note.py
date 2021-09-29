from rest_framework import serializers

from . import *
from users.serializers import UserSerializer
from ..models import Note

class NoteSerializer ( serializers.ModelSerializer ):
    model = Note

    user = UserSerializer()
    board = BoardSerializer()
    page = PageSerializer()

    tags = TagSerializer(many=True)
    assigned_to = UserSerializer()

    class Meta:
        model = Note
        fields = '__all__'
        # TODO add ordering here