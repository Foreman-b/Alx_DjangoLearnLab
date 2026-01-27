from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    query = Book.objects.all()
    serializer_class = BookSerializer


