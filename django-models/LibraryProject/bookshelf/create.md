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

Now, I create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949 with:
        >>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
        >>> book.save()

