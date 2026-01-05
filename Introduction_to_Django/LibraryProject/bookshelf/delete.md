Then I deleted the created instance with;

    >>> book = Book.objects.get(id=1)
    >>> book.delete()
    
    Output:
    (1, {'bookshelf.Book': 1})
    
Then I recheck if the created book instance is deleted or not:

    >>> Book.objects.all().values()

    Output:
    <QuerySet []>