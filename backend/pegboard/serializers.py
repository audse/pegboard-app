from rest_framework import serializers

from .models import Card, Page, Board, Folder, Theme

class CardSerializer ( serializers.ModelSerializer ):
    model = Card
    class Meta:
        model = Card
        fields = '__all__'
        # TODO add ordering here

class PageSerializer ( serializers.ModelSerializer ):
    model = Page
    class Meta:
        model = Page
        fields = '__all__'
    
class BoardSerializer ( serializers.ModelSerializer ):
    model = Board
    class Meta:
        model = Board
        fields = '__all__'

class FolderSerializer ( serializers.ModelSerializer ):
    model = Folder
    class Meta:
        model = Folder
        fields = '__all__'

class ThemeSerializer ( serializers.ModelSerializer ):
    model = Theme
    class Meta:
        model = Theme
        fields = '__all__'
