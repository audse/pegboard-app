
from rest_framework import serializers

from . import *
from users.serializers import UserSerializer
from ..models import Tag

class TagSerializer ( serializers.ModelSerializer ):
    model = Tag

    class Meta:
        model = Tag
        fields = ['id', 'name', 'color']
        depth = 1
