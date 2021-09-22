from __future__ import unicode_literals
from django.test import TestCase
from django.test.client import RequestFactory

from django.utils import timezone

from django.contrib.auth.models import User
from ..models import Folder
from ..views import FolderViewSet


class FolderTests ( TestCase ):

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

        self.field_name = 'Folder Name'
        self.field_date_archived = timezone.now()

        self.current_user_test_folder, self.user_a_test_folder = {
            'user': self.current_user,
            'name': self.field_name
        }, {
            'user': self.user_a,
            'name': self.field_name
        }

        self.request = RequestFactory().get('/folders/')
        self.request.user = self.current_user

        self.view = FolderViewSet()
        self.view.setup(self.request)
    

    '''    
    <FolderViewSet> TESTS FOR `list` FUNCTION
    '''

    def test__no_results_in_list_all(self):
        response = self.view.list(self.request)
        self.assertTrue(response.status_code != 200)

    def test__no_archived_in_list_all(self):
        Folder.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_folder
        ), Folder.objects.create(**self.current_user_test_folder)

        response = self.view.list(self.request)
        self.assertTrue(len(response.data) == 1)

    def test__only_has_permission_in_list_all(self):
        Folder.objects.create(**self.current_user_test_folder)
        Folder.objects.create(**self.user_a_test_folder)

        response = self.view.list(self.request)
        self.assertTrue(len(response.data) == 1)
    

    '''    
    <FolderViewSet> TESTS FOR `retrieve` FUNCTION
    '''

    def test__no_permission(self):
        test_folder = Folder.objects.create(**self.user_a_test_folder)
        response = self.view.retrieve(self.request, test_folder.id)
        self.assertTrue(response.status_code != 200)
        

    '''    
    <FolderViewSet> TESTS FOR `create` FUNCTION
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
    <FolderViewSet> TESTS FOR `update` FUNCTION
    '''

    def test__update_folder(self):
        test_folder = Folder.objects.create(**self.current_user_test_folder)
        self.request.data = {
            'name': 'New Folder Name'
        }
        response = self.view.update(self.request, test_folder.id)
        self.assertEqual(response.data['name'], 'New Folder Name')

    def test__update_empty_folder(self):
        test_folder = Folder.objects.create(**self.current_user_test_folder)
        self.request.data = {
            'name': None
        }
        response = self.view.update(self.request, test_folder.id)
        self.assertTrue(response.status_code != 200)
    
    def test__update_doesnt_exist(self):
        self.request.data = {
            'name': self.field_name
        }
        response = self.view.update(self.request, 1)
        self.assertTrue(response.status_code != 200)
    
    def test__update_no_permission(self):
        test_folder = Folder.objects.create(**self.user_a_test_folder)
        self.request.data = {
            'name': 'New Test Name'
        }
        response = self.view.update(self.request, test_folder.id)
        self.assertTrue(response.status_code != 200)
    


    '''    
    <FolderViewSet> TESTS FOR `list_archived` FUNCTION (ACTION)
    '''

    def test__list_archived(self):
        Folder.objects.create(**self.current_user_test_folder)
        Folder.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_folder
        )

        response = self.view.list_archived(self.request)
        self.assertTrue(len(response.data) is 1)
    
    def test__list_archived_with_no_permission(self):
        Folder.objects.create(
            date_archived=self.field_date_archived,
            **self.user_a_test_folder
        )

        response = self.view.list_archived(self.request)
        self.assertTrue(response.status_code != 200)


    '''    
    <FolderViewSet> TESTS FOR `archive` FUNCTION (ACTION)
    '''

    def test__archive(self):
        test_folder = Folder.objects.create(**self.current_user_test_folder)

        response = self.view.archive(self.request, test_folder.id)
        self.assertTrue(response.data['date_archived'] is not None)

    def test__archive_with_no_permission(self):
        test_folder = Folder.objects.create(**self.user_a_test_folder)
        response = self.view.archive(self.request, test_folder.id)
        self.assertTrue(response.status_code != 200)

    def test__archive_with_already_archived(self):
        test_folder = Folder.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_folder
        )

        response = self.view.archive(self.request, test_folder.id)
        self.assertTrue(response.data['date_archived'] is not None)

    '''    
    <FolderViewSet> TESTS FOR `unarchive` FUNCTION (ACTION)
    '''

    def test__unarchive(self):
        test_folder = Folder.objects.create(
            date_archived=self.field_date_archived,
            **self.current_user_test_folder
        )

        response = self.view.unarchive(self.request, test_folder.id)
        self.assertTrue(response.data['date_archived'] is None)

    def test__unarchive_with_no_permission(self):
        test_folder = Folder.objects.create(
            date_archived=self.field_date_archived,
            **self.user_a_test_folder
        )

        response = self.view.unarchive(self.request, test_folder.id)
        self.assertTrue(response.status_code != 200)

    def test__unarchive_with_not_archived(self):
        test_folder = Folder.objects.create(**self.current_user_test_folder)

        response = self.view.unarchive(self.request, test_folder.id)
        self.assertTrue(response.data['date_archived'] is None)


