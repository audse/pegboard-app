# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.test.client import RequestFactory

from django.utils import timezone

from django.contrib.auth.models import User
from ..models import Page, Board
from ..views import PageViewSet

class PageTests ( TestCase ):

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

        self.field_name = 'Page Name'
        self.field_date_archived = timezone.now()

        self.current_user_test_page, self.user_a_test_page = {
            'user': self.current_user,
            'name': self.field_name
        }, {
            'user': self.user_a,
            'name': self.field_name
        }

        self.request = RequestFactory().get('/pages/')
        self.request.user = self.current_user

        self.view = PageViewSet()
        self.view.setup(self.request)
    

    '''    
    <PageViewSet> TESTS FOR `list` FUNCTION
    '''

    def test__no_results_in_list_all ( self ):
        response = self.view.list(self.request)
        self.assertEqual(response.status_code, 404)

    def test__no_archived_in_list_all ( self ):
        Page.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_page
        ), Page.objects.create(**self.current_user_test_page)

        response = self.view.list(self.request)
        self.assertTrue(len(response.data) == 1)

    def test__only_has_permission_in_list_all ( self ):
        Page.objects.create(**self.current_user_test_page)
        Page.objects.create(**self.user_a_test_page)

        response = self.view.list(self.request)
        self.assertTrue(len(response.data) == 1)
    

    '''    
    <PageViewSet> TESTS FOR `retrieve` FUNCTION
    '''

    def test__no_permission ( self ):
        test_page = Page.objects.create(**self.user_a_test_page)
        response = self.view.retrieve(self.request, test_page.id)
        self.assertEqual(response.status_code, 404)
    
    def test__no_archived ( self ):
        test_page = Page.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_page
        )
        response = self.view.retrieve(self.request, test_page.id)
        self.assertEqual(response.status_code, 404)
    

    '''    
    <PageViewSet> TESTS FOR `list_by_board` FUNCTION (ACTION)
    '''
    
    def test__list_by_board_with_no_board ( self ):
        test_page = Page.objects.create(**self.current_user_test_page)
        response = self.view.list_by_board(self.request, 1)
        self.assertEqual(response.status_code, 404)
    
    def test__list_by_board_with_no_results ( self ):
        test_board = Board.objects.create(
            user=self.current_user,
            name='Test Board'
        )
        response = self.view.list_by_board(self.request, test_board.id)
        self.assertEqual(response.status_code, 404)
    
    def test__list_by_board_with_no_permission ( self ):
        test_board = Board.objects.create(
            user=self.user_a,
            name='Test Board'
        )

        Page.objects.create(
            board=test_board,
            **self.user_a_test_page
        ), Page.objects.create(
            **self.current_user_test_page
        ), Page.objects.create(
            board=test_board,
            **self.current_user_test_page
        )

        response = self.view.list_by_board(self.request, test_board.id)
        self.assertEqual(response.status_code, 404)

    def test__list_by_board_with_archived_board ( self ):
        test_board = Board.objects.create(
            user=self.current_user,
            name='Test Board',
            date_archived=self.field_date_archived
        )
        Page.objects.create(
            board=test_board,
            **self.current_user_test_page
        )
        response = self.view.list_by_board(self.request, test_board)
        self.assertEqual(response.status_code, 404)


    '''    
    <PageViewSet> TESTS FOR `create` FUNCTION
    '''

    def test__create_page ( self ):
        self.request.data = {
            'user': self.current_user.id,
            'name': self.field_name
        }
        response = self.view.create(self.request)
        self.assertEqual(response.data['name'], self.field_name)
    
    def test__create_empty_page ( self ):
        self.request.data = {}
        response = self.view.create(self.request)
        self.assertEqual(response.status_code, 400)
    
    def test__create_page_board_doesnt_exist ( self ):
        self.request.data = {
            'user': self.current_user.id,
            'name': self.field_name,
            'board': 1,
        }
        response = self.view.create(self.request)
        self.assertEqual(response.status_code, 404)

    def test__create_page_in_board_with_no_permission ( self ):
        test_board = Board.objects.create(
            user=self.user_a,
            name='Test Board'
        )
        self.request.data = {
            'user': self.current_user.id,
            'name': self.field_name,
            'board': test_board.id
        }
        response = self.view.create(self.request)
        self.assertEqual(response.status_code, 404)

    
    '''    
    <PageViewSet> TESTS FOR `update` FUNCTION
    '''

    def test__update_page ( self ):
        test_page = Page.objects.create(**self.current_user_test_page)
        self.request.data = {
            'name': 'New Page Name'
        }
        response = self.view.update(self.request, test_page.id)
        self.assertEqual(response.data['name'], 'New Page Name')

    def test__update_empty_page ( self ):
        test_page = Page.objects.create(**self.current_user_test_page)
        self.request.data = {
            'name': None
        }
        response = self.view.update(self.request, test_page.id)
        self.assertEqual(response.status_code, 400)
    
    def test__update_doesnt_exist ( self ):
        self.request.data = {
            'name': self.field_name
        }
        response = self.view.update(self.request, 1)
        self.assertEqual(response.status_code, 404)
    
    def test__update_no_permission ( self ):
        test_page = Page.objects.create(**self.user_a_test_page)
        self.request.data = {
            'name': 'New Test Name'
        }
        response = self.view.update(self.request, test_page.id)
        self.assertEqual(response.status_code, 404)
    
    def test__update_board_doesnt_exist ( self ):
        test_page = Page.objects.create(**self.current_user_test_page)
        self.request.data = {
            'board': 1
        }
        response = self.view.update(self.request, test_page.id)
        self.assertEqual(response.status_code, 400)

    def test__update_page_in_board_with_no_permission ( self ):
        test_page = Page.objects.create(**self.current_user_test_page)
        test_board = Board.objects.create(
            user=self.user_a,
            name='Test Board'
        )
        self.request.data = {
            'board': test_board.id
        }
        response = self.view.update(self.request, test_page.id)
        self.assertEqual(response.status_code, 400)


    '''    
    <PageViewSet> TESTS FOR `list_unsorted` FUNCTION (ACTION)
    '''

    # should return a list of only one unsorted <Page>
    def test__list_unsorted ( self ):
        Page.objects.create(**self.current_user_test_page)
        Page.objects.create(
            board=Board.objects.create(user=self.current_user, name='Test Board'),
            **self.current_user_test_page
        )

        response = self.view.list_unsorted(self.request)
        self.assertTrue(len(response.data) is 1)

    # should return 404 when the <User:current_user> does not have access to the requested <Page> list
    def test__list_unsorted_with_no_permission ( self ):
        Page.objects.create(**self.user_a_test_page)

        response = self.view.list_unsorted(self.request)
        self.assertEqual(response.status_code, 404)

    # should return a list of only one unsorted <Page>
    def test__list_unsorted_board_doesnt_exist ( self ):
        test_board = Board.objects.create(
            user=self.current_user,
            name='Test Board'
        )
        Page.objects.create(
            board=test_board,
            **self.current_user_test_page
        )
        test_board.delete()
        response = self.view.list_unsorted(self.request)
        self.assertTrue(len(response.data) is 1)

    # should return 404 when there are no unsorted, unarchived <Page> objects
    def test__list_unsorted_with_archived ( self ):
        Page.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_page
        )
        response = self.view.list_unsorted(self.request)
        self.assertEqual(response.status_code, 404)
        

    '''    
    <PageViewSet> TESTS FOR `list_archived` FUNCTION (ACTION)
    '''

    # should return a list containing only one archived <Page>
    def test__list_archived ( self ):
        Page.objects.create(**self.current_user_test_page)
        Page.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_page
        )

        response = self.view.list_archived(self.request)
        self.assertTrue(len(response.data) is 1)
    
    # should return 404 when the <User:current_user> does not have access to the requested <Page>
    def test__list_archived_with_no_permission ( self ):
        Page.objects.create(
            date_archived=self.field_date_archived,
            **self.user_a_test_page
        )

        response = self.view.list_archived(self.request)
        self.assertEqual(response.status_code, 404)


    '''    
    <PageViewSet> TESTS FOR `retrieve_archived` FUNCTION (ACTION)
    '''

    # should return a <Page> with a non-empty `date_archived` field
    def test__retrieve_archived ( self ):
        test_page = Page.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_page
        )

        response = self.view.retrieve_archived(self.request, test_page.id)
        self.assertTrue(response.data['date_archived'] is not None)
    
    # should return 404 when the <User:current_user> does not have access to the requested <Page>
    def test__retrieve_archived_with_no_permission ( self ):
        test_page = Page.objects.create(
            date_archived=self.field_date_archived,
            **self.user_a_test_page
        )
        response = self.view.retrieve_archived(self.request, test_page.id)
        self.assertEqual(response.status_code, 404)

    '''    
    <PageViewSet> TESTS FOR `archive` FUNCTION (ACTION)
    '''

    # should update a <Page> to a non-empty `date_archived` field
    def test__archive ( self ):
        test_page = Page.objects.create(**self.current_user_test_page)

        response = self.view.archive(self.request, test_page.id)
        self.assertTrue(response.data['date_archived'] is not None)

    # should return 404 when the <User:current_user> does not have access to the requested <Page>
    def test__archive_with_no_permission ( self ):
        test_page = Page.objects.create(**self.user_a_test_page)
        response = self.view.archive(self.request, test_page.id)
        self.assertEqual(response.status_code, 404)

    # should return a <Page> with a non-empty `date_archived` field
    def test__archive_with_already_archived ( self ):
        test_page = Page.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_page
        )

        response = self.view.archive(self.request, test_page.id)
        self.assertTrue(response.data['date_archived'] is not None)

    '''    
    <PageViewSet> TESTS FOR `unarchive` FUNCTION (ACTION)
    '''

    # should update a <Page> to an empty `date_archived` field
    def test__unarchive ( self ):
        test_page = Page.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_page
        )

        response = self.view.unarchive(self.request, test_page.id)
        self.assertTrue(response.data['date_archived'] is None)

    # should return 404 when the <User:current_user> does not have access to the requested <Page>
    def test__unarchive_with_no_permission ( self ):
        test_page = Page.objects.create(
            date_archived=self.field_date_archived,
            **self.user_a_test_page
        )

        response = self.view.unarchive(self.request, test_page.id)
        self.assertEqual(response.status_code, 404)

    # should return a <Page> with an empty `date_archived` field
    def test__unarchive_with_not_archived ( self ):
        test_page = Page.objects.create(**self.current_user_test_page)

        response = self.view.unarchive(self.request, test_page.id)
        self.assertTrue(response.data['date_archived'] is None)

