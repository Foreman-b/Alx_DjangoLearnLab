Then I deleted the created instance with;

    >>> Book.objects.get(id=1).delete()
    Output:
    (1, {'bookshelf.Book': 1})
    
Then I recheck if the created book instance is deleted or not:

    >>> Book.objects.all().values()

    Output:
    <QuerySet []>