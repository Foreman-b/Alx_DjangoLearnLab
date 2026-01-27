from django.contrib import admin
from .models import Book

# Let register Book to the database
admin.site.register(Book)
