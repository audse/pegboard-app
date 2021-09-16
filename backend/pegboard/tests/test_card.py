# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.test.client import RequestFactory

from django.utils import timezone

from django.contrib.auth.models import User
from ..models import Card, List
from ..views import CardViewSet

# TESTME test_card.py
# [ ] integration test ?
# [ ] end-to-end test ?

class CardTests ( TestCase ):

    def setUp ( self ):

        # Create Example Users
        self.current_user, self.user_a = User.objects.create_user(
            id = 1,
            username = 'current_user',
            email = 'current_user@test_user.com',
            password = 'password'
        ), User.objects.create_user(
            id = 2,
            username = 'user_a', 
            email = 'user_a@test_user.com',
            password = 'password'
        ),

        # Create Example Data
        self.field_name = 'Test Card'
        self.field_archived = timezone.now()

        self.current_user_test_card, self.user_a_test_card = {
            'user': self.current_user,
            'name': self.field_name
        }, {
            'user': self.user_a,
            'name': self.field_name
        }

        # Initialize the API for <CardViewSet>
        # which is the URL /cards/
        self.request = RequestFactory().get('/cards/')
        self.request.user = self.current_user

        # Use the <CardViewSet> for all tests
        self.view = CardViewSet()
        self.view.setup(self.request)


    '''    
    <CardViewSet> TESTS FOR `list` FUNCTION
    '''

    # no_results_in_list_all
    # ASSERTS   : should return 404 if there are no <Card> objects
    # FUNCTION : `list`
    def test__no_results_in_list_all ( self ):
        response = self.view.list(self.request)

        self.assertEqual(response.status_code, 404)

    # no_archived_in_list_all
    # ASSERTS   : should return only <Card> objects that have not been archived
    # FUNCTION : `list`
    def test__no_archived_in_list_all ( self ):
        Card.objects.create(
            date_archived = self.field_archived,
            **self.current_user_test_card
        ), Card.objects.create(**self.current_user_test_card)

        response = self.view.list(self.request)
        self.assertTrue(len(response.data) is 1)

    # only_has_permission_in_list_all
    # ASSERTS   : should return only the <User:current_user> <Card> objects
    # FUNCTION : `list`
    def test__only_has_permission_in_list_all ( self ):
        Card.objects.create(**self.current_user_test_card)
        Card.objects.create(**self.user_a_test_card)
        
        response = self.view.list(self.request)
        self.assertTrue(len(response.data) is 1)


    '''    
    <CardViewSet> TESTS FOR `retrieve` FUNCTION
    '''

    # no_permission
    # ASSERTS   : should return 404 if the <User:current_user> does not
    #             have access to the requested <Card>
    # FUNCTION : 'retrieve'
    def test__no_permission ( self ):

        test_card = Card.objects.create(**self.user_a_test_card)

        response = self.view.retrieve(self.request, test_card.id)
        self.assertEqual(response.status_code, 404)

    # no_archived
    # ASSERTS   : should return 404 if the requested <Card> is archived
    # FUNCTION : 'retrieve'
    def test__no_archived ( self ):

        test_card = Card.objects.create(
            date_archived=self.field_archived,
            **self.current_user_test_card
        )

        response = self.view.retrieve(self.request, test_card.id)
        self.assertEqual(response.status_code, 404)


    '''    
    <CardViewSet> TESTS FOR `get_by_list` FUNCTION (ACTION)
    '''

    # get_by_list_with_no_list
    # ASSERTS   : should return 404 when the requested <List> doesn't exist
    # FUNCTION : 'get_by_list'
    def test__get_by_list_with_no_list ( self ):
        Card.objects.create(**self.current_user_test_card)

        response = self.view.get_by_list(self.request, 1)
        self.assertEqual(response.status_code, 404)

    # get_by_list_with_no_results
    # ASSERTS   : `should return 404 when no <Card> objects are found
    # FUNCTION : 'get_by_list'
    def test__get_by_list_with_no_results ( self ):
        List.objects.create(
            user=self.current_user,
            name='Test List'
        )

        response = self.view.get_by_list(self.request, 1)
        self.assertEqual(response.status_code, 404)
    
    # get_by_list_with_no_permission
    # ASSERTS   : should return 404 when the <User:current_user> doesn't have access to the <List>
    # FUNCTION : 'get_by_list'
    def test__get_by_list_with_no_permission ( self ):
        current_list = List.objects.create(
            user=self.user_a,
            name='Test List'
        )

        # Create <Card> objects for both users so that the test does not give a false positive
        Card.objects.create(
            list=current_list,
            **self.user_a_test_card
        ), Card.objects.create(
            **self.current_user_test_card
        ), Card.objects.create(
            list=current_list, # This should never happen, they don't own this <List>
            **self.current_user_test_card
        )

        response = self.view.get_by_list(self.request, 1)
        self.assertEqual(response.status_code, 404)

    # get_by_list_with_archived_list
    # ASSERTS   : should return 404 when the <List> is archived, even if its' children aren't
    # FUNCTION : 'get_by_list'
    def test__get_by_list_with_archived_list ( self ):
        current_list = List.objects.create(
            user=self.current_user,
            name='Test List',
            date_archived = self.field_archived
        )
        Card.objects.create( # the <List> is archived, but it's <Card> isn't
            list=current_list,
            **self.current_user_test_card
        )

        response = self.view.get_by_list(self.request, 1)
 
        self.assertEqual(response.status_code, 404)
    

    '''    
    <CardViewSet> TESTS FOR `create` FUNCTION
    '''

    # create_card
    # ASSERTS   : should return a <Card> with an <id:Number> of 1 (the first object)
    # FUNCTION : `create`
    def test__create_card ( self ):
        self.request.data = {
            'user': 1,
            'name': self.field_name
        }
        response = self.view.create(self.request)
        self.assertEqual(response.data['id'], 1)
    
    # create_empty_card
    # ASSERTS   : should return 400 when the <Card> request does not contain required data
    # FUNCTION : `create`
    def test__create_empty_card ( self ):
        self.request.data = {}
        response = self.view.create(self.request)
        self.assertEqual(response.status_code, 400)

    # ccreate_card_list_doesnt_exist
    # ASSERTS   : should return 400 when the requested <List> doesn't exist
    # FUNCTION : `create`
    def test__create_card_list_doesnt_exist ( self ):
        self.request.data = {
            'user': 1,
            'name': self.field_name,
            'list': 1,
        }
        response = self.view.create(self.request)
        self.assertEqual(response.status_code, 400)
    
    # card_in_no_permission_list
    # ASSERTS   : should return 400 when the <User> does not have access to the requested <List>
    # FUNCTION : `create`
    def test__create_card_in_list_with_no_permission ( self ):
        List.objects.create(
            user=self.user_a,
            name='Test List'
        )
        self.request.data = {
            'user': 1,
            'name': self.field_name,
            'list': 1,
        }
        response = self.view.create(self.request)
        self.assertEqual(response.status_code, 400)
    
    # def test__update_empty_card ( self ):
    #     pass

    # TESTME <CardViewSet> `update`
    # [ ] test__update_empty_card
    # [ ] test__update_list_doesnt_exist
    # [ ] test__update_card_doesnt_exist
    # [ ] test__update_no_permission

