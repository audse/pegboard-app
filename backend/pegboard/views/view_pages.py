from __future__ import unicode_literals
from django.db.models import query
from django.http.response import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.template.defaultfilters import slugify

# from ..serializers import ProfileSerializer, CardSerializer, ListSerializer, BoardSerializer, ThemeSerializer

from django.contrib.auth.models import User
from ..models import Card, List, Board, Theme

def home_page ( request ):
    return render( request, 'pegboard/Home.page.html' )