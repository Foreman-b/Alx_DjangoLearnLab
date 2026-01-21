from relationship_app.models import Author, Book, Library, Librarian

# Let query all books by a specific author

author_name = "Durodola Adeoti"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

# Let print the list of books.
print(f"Books by {author_name}: {books_by_author}")




# Let list all the books in a library
library_name = "Nigerian Novel Books"
library = Library.objects.get(name=library_name)
# Access the ManyToMany relationship
library_books = library.books.all()
# Let print the list of books.
print(f"Books in {library_name}: {library_books}")



# Let retrieve the librarian for a library
librarian_library = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}: {library.name}")
