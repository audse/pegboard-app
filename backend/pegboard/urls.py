from django.urls import include, path
from rest_framework import routers

from . import views

# Django Rest Framework Setup
router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'cards', views.CardViewSet)
router.register(r'lists', views.ListViewSet)
router.register(r'boards', views.BoardViewSet)
router.register(r'themes', views.ThemeViewSet)

urlpatterns = [

    # Pages
    path('', views.home_page, name='home_page'),
    path('', include(router.urls)),

    path('api/', include('rest_framework.urls', namespace='rest_framework')),

]
