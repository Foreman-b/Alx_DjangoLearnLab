Now, I update my created Book instance with:

    >>> book = Book.objects.get(id=1)
    >>> book.title = "Nineteen Eighty-Four"
    >>> book.save()
    >>> book = Book.objects.all().values()
    >>> print(book)

    Output:
    <QuerySet [{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}]>