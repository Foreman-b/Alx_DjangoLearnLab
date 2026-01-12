from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library

# Let get all list of books
def list_books(request):
    books = Book.objects.all()
    
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Let Create Class-Based View for Library Details
class LibraryDetailView(DetailView):
    model = Library
    
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['books'] = self.object.books.all()
        return context
