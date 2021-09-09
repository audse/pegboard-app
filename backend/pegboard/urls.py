from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),

    path('card/<int:card_id>/<slug:card_slug>/', views.view_card, name='view_card'),
    path('card/add/', views.add_card, name='add_card'),
]