# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.test.client import RequestFactory

from django.contrib.auth.models import User
from ..models import Card
from ..views import CardViewSet

class CardTests ( TestCase ):

    def setUp ( self ):
        # Initialize the cards API
        self.request = RequestFactory().get('/cards/')

        # Initialize our pretend-user's login
        self.current_user = User.objects.create_user(
            id = 1,
            username = 'current_user',
            email = 'current_user@test_user.com',
            password = 'password'
        )
        self.request.user = self.current_user

        # Use the CardViewSet for the tests
        self.view = CardViewSet()
        self.view.setup(self.request)


    # Make sure that the test returns a message
    # when no cards are found.
    def test__no_results ( self ):
        response = self.view.list(self.request)

        ## TEST RESULTS
        self.assertEqual(response.status_code, 404)
        self.assertTrue('No cards are available.' in response.data)


    # Makes sure that you can't view a card you didn't create
    def test__no_permission ( self ):

        card = Card.objects.create(
            # Different than current user
            user = User.objects.create_user(
                id = 2,
                username = 'owner_user', 
                email = 'owner_user@test_user.com',
                password = 'password'
            ),
            name = 'Test Auth Permissions'
        )

        ## TEST RESULTS
        response = self.view.retrieve(self.request, card.id)
        self.assertEqual(response.status_code, 404)
        self.assertTrue('The card is not available.' in response.data)


# TODO test_card.py
# @ test__empty_card
# @ test__card_archived
# @ test__get_by_list_with_no_list

