from django.urls import path

from . import views

urlpatterns = [

    # Pages
    path('', views.home_page, name='home_page'),

    path('card/add/', views.add_card_page, name='add_card'),
    path('list/add/', views.add_list_page, name='add_list'),
    path('board/add/', views.add_board_page, name='add_board'),

    # API
    path('card/<int:card_id>/<slug:card_slug>/', views.view_card, name='view_card'),
]