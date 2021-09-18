from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('pegboard.urls')),
    path('accounts/', include('allauth.urls')),

    path('auth/', include('auth.urls')),
]
