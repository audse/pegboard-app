# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.test.client import RequestFactory

from django.utils import timezone

from django.contrib.auth.models import User
from ..models import Note, Page
from ..views import NoteViewSet

# TESTME test_note.py
# [ ] integration test ?
# [ ] end-to-end test ?


class NoteTests ( TestCase ):

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
        self.field_name = 'Test Note'
        self.field_archived = timezone.now()

        self.current_user_test_note, self.user_a_test_note = {
            'user': self.current_user,
            'name': self.field_name
        }, {
            'user': self.user_a,
            'name': self.field_name
        }

        # Initialize the API for <NoteViewSet>
        # which is the URL /notes/
        self.request = RequestFactory().get('/notes/')
        self.request.user = self.current_user

        # Use the <NoteViewSet> for all tests
        self.view = NoteViewSet()
        self.view.setup(self.request)


    '''    
    <NoteViewSet> TESTS FOR `list` FUNCTION
    '''

    # should return 404 if there are no <Note> objects
    def test__no_results_in_list_all ( self ):
        response = self.view.list(self.request)

        self.assertEqual(response.status_code, 404)

    # should return only <Note> objects that have not been archived
    def test__no_archived_in_list_all ( self ):
        Note.objects.create(
            date_archived = self.field_archived,
            **self.current_user_test_note
        ), Note.objects.create(**self.current_user_test_note)

        response = self.view.list(self.request)
        self.assertTrue(len(response.data) is 1)

    # should return only the <User:current_user> <Note> objects
    def test__only_has_permission_in_list_all ( self ):
        Note.objects.create(**self.current_user_test_note)
        Note.objects.create(**self.user_a_test_note)
        
        response = self.view.list(self.request)
        self.assertTrue(len(response.data) is 1)


    '''    
    <NoteViewSet> TESTS FOR `retrieve` FUNCTION
    '''

    # should return 404 if the <User:current_user> does not
    #           have access to the requested <Note>
    def test__no_permission ( self ):

        test_note = Note.objects.create(**self.user_a_test_note)

        response = self.view.retrieve(self.request, test_note.id)
        self.assertEqual(response.status_code, 404)

    # should return 404 if the requested <Note> is archived
    def test__no_archived ( self ):

        test_note = Note.objects.create(
            date_archived=self.field_archived,
            **self.current_user_test_note
        )

        response = self.view.retrieve(self.request, test_note.id)
        self.assertEqual(response.status_code, 404)


    '''    
    <NoteViewSet> TESTS FOR `list_by_page` FUNCTION (ACTION)
    '''

    # should return 404 when the requested <Page> doesn't exist
    def test__list_by_page_with_no_page ( self ):
        test_note = Note.objects.create(**self.current_user_test_note)

        response = self.view.list_by_page(self.request, 1)
        self.assertEqual(response.status_code, 404)

    # `should return 404 when no <Note> objects are found
    def test__list_by_page_with_no_results ( self ):
        current_page = Page.objects.create(
            user=self.current_user,
            name='Test Page'
        )

        response = self.view.list_by_page(self.request, current_page.id)
        self.assertEqual(response.status_code, 404)
    
    # should return 404 when the <User:current_user> doesn't have access to the <Page>
    def test__list_by_page_with_no_permission ( self ):
        current_page = Page.objects.create(
            user=self.user_a,
            name='Test Page'
        )

        # Create <Note> objects for both users so that the test does not give a false positive
        Note.objects.create(
            page=current_page,
            **self.user_a_test_note
        ), Note.objects.create(
            **self.current_user_test_note
        ), Note.objects.create(
            page=current_page, # This should never happen, they don't own this <Page>
            **self.current_user_test_note
        )

        response = self.view.list_by_page(self.request, current_page.id)
        self.assertEqual(response.status_code, 404)

    # should return 404 when the <Page> is archived, even if its' children aren't
    def test__list_by_page_with_archived_page ( self ):
        current_page = Page.objects.create(
            user=self.current_user,
            name='Test Page',
            date_archived = self.field_archived
        )
        Note.objects.create( # the <Page> is archived, but it's <Note> isn't
            page=current_page,
            **self.current_user_test_note
        )

        response = self.view.list_by_page(self.request, current_page.id)
 
        self.assertEqual(response.status_code, 404)
    

    '''    
    <NoteViewSet> TESTS FOR `create` FUNCTION
    '''

    # should return a <Note> with an <id:Number> of 1 (the first object)
    def test__create_note ( self ):
        self.request.data = {
            'user': self.current_user.id,
            'name': self.field_name
        }
        response = self.view.create(self.request)
        self.assertTrue(response.data['id'] is not None)
    
    # should return 400 when the <Note> request does not contain required data
    def test__create_empty_note ( self ):
        self.request.data = {}
        response = self.view.create(self.request)
        self.assertEqual(response.status_code, 400)

    # should return 400 when the requested <Page> doesn't exist
    def test__create_note_page_doesnt_exist ( self ):
        self.request.data = {
            'user': self.current_user.id,
            'name': self.field_name,
            'page': 1,
        }
        response = self.view.create(self.request)
        self.assertEqual(response.status_code, 400)
    
    # should return 400 when the <User:current_user> does not have access to the requested <Page>
    def test__create_note_in_page_with_no_permission ( self ):
        current_page = Page.objects.create(
            user=self.user_a,
            name='Test Page'
        )
        self.request.data = {
            'user': self.current_user.id,
            'name': self.field_name,
            'page': current_page.id,
        }
        response = self.view.create(self.request)
        self.assertEqual(response.status_code, 400)
    

    '''    
    <NoteViewSet> TESTS FOR `update` FUNCTION
    '''

    # should return the <Note> object's updated name
    def test__update_note ( self ):
        note = Note.objects.create(**self.current_user_test_note)
        self.request.data = {
            'name': 'New Test Name',
        }
        response = self.view.update(self.request, note.id)
        self.assertEqual(response.data['name'], 'New Test Name')

    # should return 400 when the <Note> request removes required data
    def test__update_empty_note ( self ):
        note = Note.objects.create(**self.current_user_test_note)
        self.request.data = {
            'name': None,
        }
        response = self.view.update(self.request, note.id)
        self.assertEqual(response.status_code, 400)
    
    # should return 404 when the requested <Note> doesn't exist
    def test__update_doesnt_exist ( self ):
        self.request.data = {
            'name': self.field_name
        }
        response = self.view.update(self.request, 1)
        self.assertEqual(response.status_code, 404)
    
    # should return 400 when the <User:current_user> does not have access to the requested <Note>
    def test__update_no_permission ( self ):
        note = Note.objects.create(**self.user_a_test_note)
        self.request.data = {
            'name': 'New Test Name'
        }
        response = self.view.update(self.request, note.id)
        self.assertEqual(response.status_code, 404)

    # should return 400 when the requested <Page> doesn't exist
    def test__update_page_doesnt_exist ( self ):
        note = Note.objects.create(**self.current_user_test_note)
        self.request.data = {
            'page': 1
        }
        response = self.view.update(self.request, note.id)
        self.assertEqual(response.status_code, 400)

    # should return 400 when the <User:current_user> does not have access to the requested <Page>
    def test__update_note_in_page_with_no_permission ( self ):
        note = Note.objects.create(**self.current_user_test_note)
        current_page = Page.objects.create(
            user=self.user_a,
            name='Test Page'
        )
        self.request.data = {
            'page': current_page.id
        }
        response = self.view.update(self.request, note.id)
        self.assertEqual(response.status_code, 400)


    '''    
    <NoteViewSet> TESTS FOR `list_unsorted` FUNCTION (ACTION)
    '''

    # should return a list of only one unsorted <Note>
    def test__list_unsorted ( self ):
        Note.objects.create(**self.current_user_test_note)
        Note.objects.create(
            page=Page.objects.create(user=self.current_user, name='Test Page'),
            **self.current_user_test_note
        )

        response = self.view.list_unsorted(self.request)
        self.assertTrue(len(response.data) is 1)

    # should return 404 when the <User:current_user> does not have access to the requested <Note> list
    def test__list_unsorted_with_no_permission ( self ):
        Note.objects.create(**self.user_a_test_note)

        response = self.view.list_unsorted(self.request)
        self.assertEqual(response.status_code, 404)

    # should return a list of only one unsorted <Note>
    def test__list_unsorted_page_doesnt_exist ( self ):
        test_page = Page.objects.create(
            user=self.current_user,
            name='Test Page'
        )
        Note.objects.create(
            page=test_page,
            **self.current_user_test_note
        )
        test_page.delete()
        response = self.view.list_unsorted(self.request)
        self.assertTrue(len(response.data) is 1)


    '''    
    <NoteViewSet> TESTS FOR `list_archived` FUNCTION (ACTION)
    '''

    # should return a list containing only one archived <Note>
    def test__list_archived ( self ):
        Note.objects.create(**self.current_user_test_note)
        Note.objects.create(
            date_archived=self.field_archived,
            **self.current_user_test_note
        )

        response = self.view.list_archived(self.request)
        self.assertTrue(len(response.data) is 1)
    
    # should return 404 when the <User:current_user> does not have access to the requested <Note>
    def test__list_archived_with_no_permission ( self ):
        Note.objects.create(
            date_archived=self.field_archived,
            **self.user_a_test_note
        )

        response = self.view.list_archived(self.request)
        self.assertEqual(response.status_code, 404)


    '''    
    <NoteViewSet> TESTS FOR `retrieve_archived` FUNCTION (ACTION)
    '''

    # should return a <Note> with a non-empty `date_archived` field
    def test__retrieve_archived ( self ):
        test_note = Note.objects.create(
            date_archived=self.field_archived,
            **self.current_user_test_note
        )

        response = self.view.retrieve_archived(self.request, test_note.id)
        self.assertTrue(response.data['date_archived'] is not None)
    
    # should return 404 when the <User:current_user> does not have access to the requested <Note>
    def test__retrieve_archived_with_no_permission ( self ):
        test_note = Note.objects.create(
            date_archived=self.field_archived,
            **self.user_a_test_note
        )
        response = self.view.retrieve_archived(self.request, test_note.id)
        self.assertEqual(response.status_code, 404)

    '''    
    <NoteViewSet> TESTS FOR `archive` FUNCTION (ACTION)
    '''

    # should update a <Note> to a non-empty `date_archived` field
    def test__archive ( self ):
        test_note = Note.objects.create(**self.current_user_test_note)

        response = self.view.archive(self.request, test_note.id)
        self.assertTrue(response.data['date_archived'] is not None)

    # should return 404 when the <User:current_user> does not have access to the requested <Note>
    def test__archive_with_no_permission ( self ):
        test_note = Note.objects.create(**self.user_a_test_note)
        response = self.view.archive(self.request, test_note.id)
        self.assertEqual(response.status_code, 404)

    # should return a <Note> with a non-empty `date_archived` field
    def test__archive_with_already_archived ( self ):
        test_note = Note.objects.create(
            date_archived=self.field_archived,
            **self.current_user_test_note
        )

        response = self.view.archive(self.request, test_note.id)
        self.assertTrue(response.data['date_archived'] is not None)

    '''    
    <NoteViewSet> TESTS FOR `unarchive` FUNCTION (ACTION)
    '''

    # should update a <Note> to an empty `date_archived` field
    def test__unarchive ( self ):
        test_note = Note.objects.create(
            date_archived=self.field_archived,
            **self.current_user_test_note
        )

        response = self.view.unarchive(self.request, test_note.id)
        self.assertTrue(response.data['date_archived'] is None)

    # should return 404 when the <User:current_user> does not have access to the requested <Note>
    def test__unarchive_with_no_permission ( self ):
        test_note = Note.objects.create(
            date_archived=self.field_archived,
            **self.user_a_test_note
        )

        response = self.view.unarchive(self.request, test_note.id)
        self.assertEqual(response.status_code, 404)

    # should return a <Note> with an empty `date_archived` field
    def test__unarchive_with_not_archived ( self ):
        test_note = Note.objects.create(**self.current_user_test_note)

        response = self.view.unarchive(self.request, test_note.id)
        self.assertTrue(response.data['date_archived'] is None)

