After I create a Book instance, then I go ahead and retrive data created with:

    >>> book = Book.objects.all().values()
    >>> print(x)

    Output:
    <QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>

