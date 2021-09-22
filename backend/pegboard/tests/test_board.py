
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.test.client import RequestFactory

from django.utils import timezone

from django.contrib.auth.models import User
from ..models import Board, Folder, Page, Note
from ..views import BoardViewSet


class BoardTests ( TestCase ):

    def setUp(self):

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

        self.field_name = 'Board Name'
        self.field_date_archived = timezone.now()

        self.current_user_test_board, self.user_a_test_board = {
            'user': self.current_user,
            'name': self.field_name
        }, {
            'user': self.user_a,
            'name': self.field_name
        }

        self.current_user_test_page, self.user_a_test_page = {
            'user': self.current_user,
            'name': 'Page Name',
        }, {
            'user': self.user_a,
            'name': 'Page Name',
        }

        self.request = RequestFactory().get('/boards/')
        self.request.user = self.current_user

        self.view = BoardViewSet()
        self.view.setup(self.request)
    

    '''    
    <BoardViewSet> TESTS FOR `list` FUNCTION
    '''

    def test__no_results_in_list_all(self):
        response = self.view.list(self.request)
        self.assertTrue(response.status_code != 200)

    def test__no_archived_in_list_all(self):
        Board.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_board
        ), Board.objects.create(**self.current_user_test_board)

        response = self.view.list(self.request)
        self.assertTrue(len(response.data) == 1)

    def test__only_has_permission_in_list_all(self):
        Board.objects.create(**self.current_user_test_board)
        Board.objects.create(**self.user_a_test_board)

        response = self.view.list(self.request)
        self.assertTrue(len(response.data) == 1)
    
    def test__list_with_shared_with(self):
        test_board = Board.objects.create(**self.user_a_test_board)
        test_board.shared_with.add(self.current_user)

        response = self.view.list(self.request)
        self.assertTrue(len(response.data) == 1)
    

    '''    
    <BoardViewSet> TESTS FOR `list_children` FUNCTION
    '''

    def test__list_children(self):
        test_board = Board.objects.create(**self.current_user_test_board)
        Page.objects.create(
            board=test_board,
            **self.current_user_test_page
        )

        response = self.view.list_children(self.request, test_board.id)
        self.assertTrue(len(response.data) == 1)
    
    def test__list_no_children(self):
        test_board = Board.objects.create(**self.current_user_test_board)
        Page.objects.create(**self.current_user_test_page)

        response = self.view.list_children(self.request, test_board.id)
        self.assertTrue(response.status_code != 200)

    def test__list_archived_children(self):
        test_board = Board.objects.create(**self.current_user_test_board)
        Page.objects.create(
            board=test_board,
            date_archived=self.field_date_archived,
            **self.user_a_test_page
        )

        response = self.view.list_children(self.request, test_board.id)
        self.assertTrue(response.status_code != 200)

    
    '''
    <BoardViewSet> TESTS FOR `list_grandchildren` FUNCTION
    '''

    def test__list_children(self):
        test_board = Board.objects.create(**self.current_user_test_board)
        test_page = Page.objects.create(
            board=test_board,
            **self.current_user_test_page
        )
        Note.objects.create(
            user=self.current_user,
            board=test_board,
            page=test_page,
            name='Test Note'
        )

        response = self.view.list_children(self.request, test_board.id)
        self.assertTrue(len(response.data) == 1)


    '''
    <BoardViewSet> TESTS FOR `list_shared_with` FUNCTION
    '''

    def test__list_shared_with(self):
        test_board = Board.objects.create(**self.user_a_test_board)
        test_board.shared_with.add(self.current_user)

        response = self.view.list_shared_with(self.request)
        self.assertTrue(len(response.data) == 1)

    '''    
    <BoardViewSet> TESTS FOR `retrieve` FUNCTION
    '''

    def test__no_permission(self):
        test_board = Board.objects.create(**self.user_a_test_board)
        response = self.view.retrieve(self.request, test_board.id)
        self.assertTrue(response.status_code != 200)
    

    '''    
    <BoardViewSet> TESTS FOR `create` FUNCTION
    '''

    def test__create_list(self):
        self.request.data = {
            'user': self.current_user.id,
            'name': self.field_name
        }
        response = self.view.create(self.request)
        self.assertEqual(response.data['name'], self.field_name)
    
    def test__create_empty_list(self):
        self.request.data = {}
        response = self.view.create(self.request)
        self.assertTrue(response.status_code != 200)

    
    '''    
    <BoardViewSet> TESTS FOR `update` FUNCTION
    '''

    def test__update_board(self):
        test_board = Board.objects.create(**self.current_user_test_board)
        self.request.data = {
            'name': 'New Board Name'
        }
        response = self.view.update(self.request, test_board.id)
        self.assertEqual(response.data['name'], 'New Board Name')

    def test__update_empty_board(self):
        test_board = Board.objects.create(**self.current_user_test_board)
        self.request.data = {
            'name': None
        }
        response = self.view.update(self.request, test_board.id)
        self.assertTrue(response.status_code != 200)
    
    def test__update_doesnt_exist(self):
        self.request.data = {
            'name': self.field_name
        }
        response = self.view.update(self.request, 1)
        self.assertTrue(response.status_code != 200)
    
    def test__update_no_permission(self):
        test_board = Board.objects.create(**self.user_a_test_board)
        self.request.data = {
            'name': 'New Test Name'
        }
        response = self.view.update(self.request, test_board.id)
        self.assertTrue(response.status_code != 200)


    '''    
    <BoardViewSet> TESTS FOR `list_by_shared_with` FUNCTION
    '''

    def test__list_shared_with(self):
        test_board_a = Board.objects.create(**self.user_a_test_board)
        test_board_a.shared_with.add(self.current_user)

        response = self.view.list_shared_with(self.request)
        self.assertTrue(len(response.data) == 1)

    '''    
    <BoardViewSet> TESTS FOR `list_unsorted` FUNCTION
    '''

    # should return a list of only one unsorted <Board>
    def test__list_unsorted(self):
        Board.objects.create(**self.current_user_test_board)
        Board.objects.create(
            folder=Folder.objects.create(user=self.current_user, name='Test Folder'),
            **self.current_user_test_board
        )

        response = self.view.list_unsorted(self.request)
        self.assertTrue(len(response.data) is 1)

    # should return 404 when the <User:current_user> does not have access to the requested <Board> list
    def test__list_unsorted_with_no_permission(self):
        Board.objects.create(**self.user_a_test_board)

        response = self.view.list_unsorted(self.request)
        self.assertTrue(response.status_code != 200)

    # should return a list of only one unsorted <Board>
    def test__list_unsorted_folder_doesnt_exist(self):
        test_folder = Folder.objects.create(
            user=self.current_user,
            name='Test Folder'
        )
        Board.objects.create(
            folder=test_folder,
            **self.current_user_test_board
        )
        test_folder.delete()
        response = self.view.list_unsorted(self.request)
        self.assertTrue(len(response.data) is 1)

    # should return 404 when there are no unsorted, unarchived <Board> objects
    def test__list_unsorted_with_archived(self):
        Board.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_board
        )
        response = self.view.list_unsorted(self.request)
        self.assertTrue(response.status_code != 200)
        

    '''    
    <BoardViewSet> TESTS FOR `list_archived` FUNCTION
    '''

    # should return a list containing only one archived <Board>
    def test__list_archived(self):
        Board.objects.create(**self.current_user_test_board)
        Board.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_board
        )

        response = self.view.list_archived(self.request)
        self.assertTrue(len(response.data) is 1)
    
    # should return 404 when the <User:current_user> does not have access to the requested <Board>
    def test__list_archived_with_no_permission(self):
        Board.objects.create(
            date_archived=self.field_date_archived,
            **self.user_a_test_board
        )

        response = self.view.list_archived(self.request)
        self.assertTrue(response.status_code != 200)

    '''    
    <BoardViewSet> TESTS FOR `archive` FUNCTION
    '''

    # should update a <Board> to a non-empty `date_archived` field
    def test__archive(self):
        test_board = Board.objects.create(**self.current_user_test_board)

        response = self.view.archive(self.request, test_board.id)
        self.assertTrue(response.data['date_archived'] is not None)

    # should return 404 when the <User:current_user> does not have access to the requested <Board>
    def test__archive_with_no_permission(self):
        test_board = Board.objects.create(**self.user_a_test_board)
        response = self.view.archive(self.request, test_board.id)
        self.assertTrue(response.status_code != 200)

    # should return a <Board> with a non-empty `date_archived` field
    def test__archive_with_already_archived(self):
        test_board = Board.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_board
        )

        response = self.view.archive(self.request, test_board.id)
        self.assertTrue(response.data['date_archived'] is not None)

    '''    
    <BoardViewSet> TESTS FOR `unarchive` FUNCTION
    '''

    # should update a <Board> to an empty `date_archived` field
    def test__unarchive(self):
        test_board = Board.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_board
        )

        response = self.view.unarchive(self.request, test_board.id)
        self.assertTrue(response.data['date_archived'] is None)

    # should return 404 when the <User:current_user> does not have access to the requested <Board>
    def test__unarchive_with_no_permission(self):
        test_board = Board.objects.create(
            date_archived=self.field_date_archived,
            **self.user_a_test_board
        )

        response = self.view.unarchive(self.request, test_board.id)
        self.assertTrue(response.status_code != 200)

    # should return a <Board> with an empty `date_archived` field
    def test__unarchive_with_not_archived(self):
        test_board = Board.objects.create(**self.current_user_test_board)

        response = self.view.unarchive(self.request, test_board.id)
        self.assertTrue(response.data['date_archived'] is None)

