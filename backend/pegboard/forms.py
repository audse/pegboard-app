
from django import forms

DISPLAY_CHOICES = ['card', 'header']

class CardForm( forms.Form ):
    name = forms.CharField(label='Card Name', max_length=128)
    content = forms.CharField(label='Card Content', widget=forms.Textarea, required=False)

    display = forms.CharField(max_length=36, widget=forms.Select(choices=DISPLAY_CHOICES))

    date_due = forms.CharField(max_length=256, required=False)
    date_todo = forms.CharField(max_length=256, required=False)

class ListForm( forms.Form ):
    name = forms.CharField(label='List Name', max_length=128, required=False)
    description = forms.CharField(label='List Description', widget=forms.Textarea)

class BoardForm( forms.Form ):
    name = forms.CharField(label='Board Name', max_length=128, required=False)
    description = forms.CharField(label='Board Description', widget=forms.Textarea)
