from rest_framework import serializers

from . import *
from ..models import Note, Board, Page

class NoteSerializer ( serializers.ModelSerializer ):
    model = Note

    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all(), allow_null=True)
    page = serializers.PrimaryKeyRelatedField(queryset=Page.objects.all(), allow_null=True)

    tags = TagSerializer(many=True, required=False)
    
    comments = CommentSerializer(many=True, required=False)
    checklists = ChecklistSerializer(many=True, required=False)

    class Meta:
        model = Note
        fields = '__all__'
        depth = 2
        # TODO add ordering here

    def update(self, instance, validated_data):

        instance.user = validated_data.get('user', instance.user)
        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)

        if validated_data.get('date_archived'):
            instance.date_archived = validated_data.get('date_archived', instance.date_archived)

        if validated_data.get('tags'):
            instance.tags.clear()
            for tag in validated_data.get('tags'):
                instance.tags.add(tag.get('id'))

        instance.save()

        return instance