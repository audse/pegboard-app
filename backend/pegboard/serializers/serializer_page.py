from rest_framework import serializers

from . import *
from users.serializers import UserSerializer
from ..models import Page

class PageSerializer ( serializers.ModelSerializer ):
    model = Page

    user = UserSerializer()
    board = BoardSerializer()
    assigned_to = UserSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Page
        fields = '__all__'