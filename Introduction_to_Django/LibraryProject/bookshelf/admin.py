from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    listdisplay = ('title', 'author', 'publication_year')
    listfilter = ('author', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
