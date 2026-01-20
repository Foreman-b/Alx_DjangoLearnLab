Now, I update my created Book instance with:

Now, I update my created Book instance with:

    >>> book = Book.objects.get(id=1)
    >>> book.title = "Nineteen Eighty-Four"
    >>> book.save()

Then I recheck with:

    >>> book =  Book.objects.get(id=1)
    >>> print(book)

    Output:
    <QuerySet [{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}]>