from rest_framework import serializers

from ..models import Note

class NoteSerializer ( serializers.ModelSerializer ):
    model = Note
    class Meta:
        model = Note
        fields = '__all__'
        # TODO add ordering here