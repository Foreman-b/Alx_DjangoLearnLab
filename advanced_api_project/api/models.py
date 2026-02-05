from django.db import models


class Author(models.Model):
    """
    Let represent a book author and this is
    One-to-Many relationship.
    """
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Let represent a book entry, each book is 
    linked to a single author through ForeignKey
    this is 'Many' side of the relationship.
    """
    title = models.CharField(max_length=225)
    publication_year = models.DateTimeField()
    # related name will allows us to access an author's books
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title