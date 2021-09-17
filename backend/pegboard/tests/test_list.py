# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.test.client import RequestFactory

from django.utils import timezone

from django.contrib.auth.models import User
from ..models import List, Board
from ..views import ListViewSet

class ListTests ( TestCase ):

    def setUp ( self ):

        self.current_user, self.user_a = User.objects.create_user(
            id=1,
            username='current_user',
            email='current_user@test_user.com',
            password='password',
        ), User.objects.create_user(
            id=2,
            username='user_a',
            email='user_a@test_user.com',
            password='password'
        )

        self.field_name = 'List Name',
        self.field_date_archived = timezone.now()

        self.current_user_test_list, self.user_a_test_list = {
            'user': self.current_user,
            'name': self.field_name
        }, {
            'user': self.user_a,
            'name': self.field_name
        }

        self.request = RequestFactory.get('/lists/')
        self.request.user = self.current_user

        self.view = ListViewSet()
        self.view.setup(self.request)
    

    '''    
    <ListViewSet> TESTS FOR `list` FUNCTION
    '''

    def test__no_results_in_list_all ( self ):
        response = self.view.list(self.request)
        self.assertEqual(response.status_code, 404)

    def test__no_archived_in_list_all ( self ):
        List.objects.create(
            date_archived=self.field_archived,
            **self.current_user_test_list
        ), List.objects.create(**self.current_user_test_list)

        response = self.view.list(self.request)
        self.assertTrue(len(response.data) is 1)

    def test__only_has_permission_in_list_all ( self ):
        List.objects.create(**self.current_user_test_list)
        List.objects.create(**self.user_a_test_list)

        response = self.view.list(self.request)
        self.assertTrue(len(response.data) is 1)
    

    '''    
    <ListViewSet> TESTS FOR `retrieve` FUNCTION
    '''

    def test__no_permission ( self ):
        test_list = List.objects.create(**self.user_a_test_list)
        response = self.view.retrieve(self.request, test_list.id)
        self.assertEqual(response.status_code, 404)
    
    def test__no_archived ( self ):
        test_list = List.objects.create(
            date_archived=self.field_archived,
            **self.current_user_test_list
        )
        response = self.view.retrieve(self.request, test_list.id)
        self.assertEqual(response.status_code, 404)
    

    '''    
    <ListViewSet> TESTS FOR `get_by_board` FUNCTION (ACTION)
    '''
    
    def test__get_by_board_with_no_board ( self ):
        test_list = List.objects.create(**self.current_user_test_list)
        response = self.view.get_by_board(self.request, 1)
        self.assertEqual(response.status_code, 404)
    
    def test__get_by_board_with_no_results ( self ):
        test_board = Board.objects.create(
            user=self.current_user,
            name='Test Board'
        )
        response = self.view.get_by_board(self.request, test_board.id)
        self.assertEqual(response.status_code, 404)
    
    def test__get_by_board_with_no_permission ( self ):
        test_board = Board.objects.create(
            user=self.user_a,
            name='Test Board'
        )

        List.objects.create(
            board=test_board,
            **self.user_a_test_list
        ), List.objects.create(
            **self.current_user_test_list
        ), List.objects.create(
            board=test_board,
            **self.current_user_test_list
        )

        response = self.view.get_by_board(self.request, test_board.id)
        self.assertEqual(response.status_code, 404)

    def test__get_by_board_with_archived_board ( self ):
        test_board = Board.objects.create(
            user=self.current_user,
            name='Test Board',
            date_archived=self.field_date_archived
        )
        List.objects.create(
            board=test_board,
            **self.current_user_test_list
        )
        response = self.view.get_by_board(self.request, test_board)
        self.assertEqual(response.status_code, 404)

