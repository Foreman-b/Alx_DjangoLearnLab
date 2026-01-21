from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book



@permission_required('bookshel.can_view', raise_exception=True)
def can_view_book(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/can_view_book.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def can_create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        
        Book.objects.create(title=title, author_id=author_id)
        return redirect('can_view_book')
    return render(request, 'bookshelf/can_create_book.html')



@permission_required('bookshelf.can_edit', raise_exception=True)
def can_edit_book(request, pk):
    books = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        books.title = request.POST.get('title')
        books.save()
        return redirect('can_view_book')
    return render(request, 'bookshelf/can_edit_book.html', {'books': books})


@permission_required('bookshelf.can_delete', raise_exception=True)
def can_delete_book(request, pk):
    books = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        books.delete()
        return redirect('can_view_book')
        #Let get the request to show confirmation page
    return render(request, 'bookshelf/can_delete_book.html', {'books': books})


