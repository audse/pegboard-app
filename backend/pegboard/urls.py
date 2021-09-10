from django.urls import include, path
from rest_framework import routers

from . import views

# Django Rest Framework Setup
router = routers.DefaultRouter()
router.register(r'cards', views.CardViewSet)
router.register(r'lists', views.ListViewSet)
router.register(r'boards', views.BoardViewSet)

urlpatterns = [

    # Pages
    path('', views.home_page, name='home_page'),
    path('', include(router.urls)),

    # Django Rest Framework API
    path('api/', include('rest_framework.urls', namespace='rest_framework')),

    # path('card/add/', views.add_card_page, name='add_card'),
    # path('list/add/', views.add_list_page, name='add_list'),
    # path('board/add/', views.add_board_page, name='add_board'),

    # API
    # path('card/<int:card_id>/<slug:card_slug>/', views.view_card, name='view_card'),
    # path('list/<int:list_id>/<slug:list_slug>/', views.view_card, name='view_list'),
    # path('board/<int:board_id>/<slug:board_slug>/', views.view_card, name='view_board'),
]
