from rest_framework import serializers

from ..models import Tag

class TagSerializer ( serializers.ModelSerializer ):
    model = Tag
    class Meta:
        model = Tag
        fields = '__all__'
