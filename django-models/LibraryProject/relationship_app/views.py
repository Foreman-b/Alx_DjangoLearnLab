from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


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

# Let allow user to register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
        # If form is NOT valid, it skips the if-block above
    else:
        form = UserCreationForm()
    
    # This return MUST be outside the if/else blocks to catch all cases
    return render(request, 'relationship_app/register.html', {'form': form})


# Let allow user to login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# Let logout the user
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')