from rest_framework import serializers

from . import *
from ..models import Note

class NoteSerializer ( serializers.ModelSerializer ):
    model = Note

    tags = TagSerializer(many=True)
    
    comments = CommentSerializer(many=True)
    checklists = ChecklistSerializer(many=True)

    class Meta:
        model = Note
        fields = '__all__'
        depth = 2
        # TODO add ordering here

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)
        
        instance.tags.clear()
        for tag in validated_data.get('tags'):
            instance.tags.add(tag.get('id'))

        instance.save()

        return instance