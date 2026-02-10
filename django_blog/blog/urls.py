from django.urls import path
from . import views
from .views import (
    PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, 
    CommentCreateView, CommentUpdateView, CommentDeleteView,
)


urlpatterns = [
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-edit"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/", PostListView.as_view(), name="posts"),
    
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-edit"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

    path('search/', views.search, name='search'),
    path('tags/<str:tag_name>/', views.PostByTagListView.as_view(), name='tagged-posts'),


    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),    
    
]