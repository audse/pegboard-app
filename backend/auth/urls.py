from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework.authtoken import views
from .views import GoogleLogin

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('token/', views.obtain_auth_token),
    path('google/', GoogleLogin.as_view(), name='google_login')
]