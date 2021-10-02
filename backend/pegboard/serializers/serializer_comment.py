from rest_framework import serializers

from ..models import Comment
    
class CommentSerializer ( serializers.ModelSerializer ):

    model = Comment

    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1