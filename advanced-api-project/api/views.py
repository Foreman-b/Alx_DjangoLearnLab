from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, permissions



class BookListView(generics.ListCreateAPIView):
    """
    GET allowed everyone to as ReadOnly and 
    POST allow only authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET allowed everyone to as ReadOnly and 
    PUT/PATCH/DELETE allow only authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]