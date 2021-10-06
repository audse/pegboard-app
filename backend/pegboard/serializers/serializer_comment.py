from rest_framework import serializers

from ..models import Comment, Board, Page, Note
    
class CommentSerializer ( serializers.ModelSerializer ):

    model = Comment

    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all(), required=False, allow_null=True)
    page = serializers.PrimaryKeyRelatedField(queryset=Page.objects.all(), required=False, allow_null=True)
    note = serializers.PrimaryKeyRelatedField(queryset=Note.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1