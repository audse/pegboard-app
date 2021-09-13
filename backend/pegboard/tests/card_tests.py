# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.test.client import RequestFactory

from django.contrib.auth.models import User
from ..models import Card
from ..views import CardViewSet

class CardTests ( TestCase ):

    def setUp ( self ):
        self.factory = RequestFactory()
        self.current_user = User.objects.create_user(
            id = 1,
            username = 'current_user',
            email = 'current_user@test_user.com',
            password = 'password'
        )

    # Make sure that the test returns a message
    # when no cards are found.
    def test__no_results ( self ):
        request = self.factory.get( '/cards/' )
        request.user = self.current_user
        view = CardViewSet()
        view.setup(request)
        response = view.list(request)

        self.assertEqual( response.status_code, 404 )
        self.assertEqual( response.data['message'], 'No cards are available.' )


    # Makes sure that you can't view a card you didn't create
    def test__auth_permissions ( self ):

        # Create the owner of the card
        # who is not the same as the current user
        owner_user = User.objects.create_user(
            id = 2,
            username = 'owner_user', 
            email = 'owner_user@test_user.com',
            password = 'password'
        )

        # Create the card the current user is
        # attempting to view
        card = Card.objects.create(
            user = owner_user,
            name = 'Test Auth Permissions',
        )

        # Request the card
        request = self.factory.get( '/cards/' )
        request.user = self.current_user
        view = CardViewSet()
        view.setup(request)
        response = view.retrieve(request, card.id)

        # Query for the card: should come up empty
        self.assertEqual( response.status_code, 404 )
        self.assertEqual( response.data['message'], 'The card is not available.' )

