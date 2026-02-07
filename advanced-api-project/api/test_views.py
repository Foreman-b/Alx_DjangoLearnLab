from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Let create a user for authentication tests
        self.user = User.objects.create_user(username='foremanb', password='password123')
        
        # Create an author (ForeignKey requirement)
        self.author = Author.objects.create(name="Foreman-B")
        
        # Create a sample book
        self.book = Book.objects.create(
            title="Mothers of Dragons",
            author=self.author,
            publication_year="2025-02-02"
        )
        
        # Define URLs using names from your urls.py
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.id})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.id})
    

    def test_create_book(self):
        """Let Test Step 3: By Creating a Book (POST)"""
        self.client.login(username='foremanb', password='password123')
        data = {
            "title": "A New Era",
            "author": self.author.id,
            "publication_year": "2026-01-01"
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Testing Step 3: By Updating a Book (PUT)"""
        self.client.login(username='foremanb', password='password123')
        data = {"title": "Updated Title", "author": self.author.id, "publication_year": "2025-02-02"}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        """Test Step 3: Deleting a Book (DELETE)"""
        self.client.login(username='foremanb', password='password123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    
    def test_search_functionality(self):
        """Test Step 1: Searching for books by title"""
        response = self.client.get(self.list_url, {'search': 'Mothers'})
        self.assertEqual(len(response.data), 1)
        self.assertIn('Mothers', response.data[0]['title'])

    def test_ordering_functionality(self):
        """Test Step 1: Ordering books by publication_year"""
        # Add another book for comparison
        Book.objects.create(title="Old Book", author=self.author, publication_year="1990-01-01")
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        # The 1990 book should come first
        self.assertEqual(response.data[0]['title'], "Old Book")

    
    def test_permissions_enforced(self):
        """Test Step 3: Ensure anonymous users cannot delete"""
        self.client.logout()
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)