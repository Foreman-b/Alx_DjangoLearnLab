from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required


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


def is_admin(user):
    return user.is_authenticated and user.profile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.profile.role == 'Member'



# 1. Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})

# 2. Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome, Librarian!'})

# 3. Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# LetAdd Book View
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        # Logic to save the book
        pass
    return render(request, 'relationship_app/add_book.html')

# Let Edit Book View
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Logic to update the book
        pass
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# Let Delete Book View
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        pass
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
