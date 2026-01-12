from django.urls import path
from . import views

urlpatterns = [
    # 1. Changed views.ListView to views.list_books
    path('list_books/', views.list_books, name='list_books'),

    # 2. Changed LibraryDetailView to views.LibraryDetailView
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
