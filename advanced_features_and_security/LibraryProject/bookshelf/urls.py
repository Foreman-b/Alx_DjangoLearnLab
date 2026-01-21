from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('can_view_book/', views.can_view_book, name='can_view_book'),
    path('can_create_book/', views.can_create_book, name='can_create_book'),
    path('can_edit_book/<int:pk>/', views.can_edit_book, name='can_edit_book'),
    path('can_delete_book/<int:pk>/', views.can_delete_book, name='can_delete_book'),
    path('form_example/', views.form_example, name='form_example'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
