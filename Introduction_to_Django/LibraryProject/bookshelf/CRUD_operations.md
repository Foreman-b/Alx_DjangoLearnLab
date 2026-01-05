CREATION OF APP

bookshelp app was created using "python manage.py startapp bookshelf", then in bookself/models.py I define Book models with title, author and publication year.

After Book models creation, I go ahead and run these two command:

        python manage.py makemigrations

        python manage.py migrate

Then, I go to my gitbash and run:
    python manage.py shell

Then I check my database with:
        >>> from bookshelf.models import Book
        >>> book = Book.objects.all()
        >>> print(x)
        <QuerySet []>

        I see my database is empty.



CREATION OF A BOOK INSTANCE

Now, I create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949 with:
        >>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
        >>> book.save()


RETRIEVE THE BOOK CREATED

After I create a Book instance, then I go ahead and retrive data created with:

    >>> book = Book.objects.get(titled="1984")
    >>> print(book)

    Output:
    <QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>



UPDATE THE TITLE OF BOOK CREATED

Now, I update my created Book instance with:

    >>> book = Book.objects.get(id=1)
    >>> book.title = "Nineteen Eighty-Four"
    >>> book.save()

Then I recheck with:
    >>> book =  Book.objects.get(id=1)
    >>> print(book)

    Output:
    <QuerySet [{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}]>


DELETE THE BOOK INSTANCE

Then I deleted the created instance with;

    >>> Book.objects.get(id=1).delete()
    Output:
    (1, {'bookshelf.Book': 1})
    
Then I recheck if the created book instance is deleted or not:

    >>> Book.objects.all().values()

    Output:
    <QuerySet []>
