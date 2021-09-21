from __future__ import unicode_literals
from django.shortcuts import render

def home_page ( request ):
    return render( request, 'pegboard/Home.page.html' )