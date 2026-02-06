from django.urls import path
from .views import BookListView, BookDetailView



urlpatterns = [
     # ListView and CreateView share this endpoint
    path('book/', BookListView.as_view(), name='book-list'),

    # DetailView, UpdateView, and DeleteView share this endpoint
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-details'),
]