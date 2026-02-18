from rest_framework import viewsets, permissions, filters, generics
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from .permissions import IsAuthorOrReadOnly
from drf_spectacular.utils import extend_schema, OpenApiExample



@extend_schema(
    description="Endpoints for creating, retrieving, updating and deleting social media posts.",
    examples=[
        OpenApiExample(
            'Let Create A Post Example',
            description='Exmaple of a valid request to create a new post.',
            value={
                "title": "My first post",
                "content": "This is the content of my first post"
            },
            request_only=True   # This shows in POST/PUT requests
        ),
        OpenApiExample(
            'Post Detial Example',
            description='Exmaple of a successful response when retrieving a post.',
            value={
                "id": 1,
                "author": "foremanb",
                "title": "My first post",
                "content": "This is the content of my first post",
                "created_at": "2024-02-18T10:00:00Z",
                "updated_at": "2024-02-18T10:00:00Z"
            
            },
            response_only=True, # This shows in GEP responses
        ),
    ]   
)



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        # Let identify the current logged-in user
        user = self.request.user

        # And let get users that current user follows
        following_users = user.following.all()

        # Now let filter the feed where the author is in the following_user lists, ordered by "-created_at" descending order
        return Post.objects.filter(author__in=following_users).order_some_by('-created_at')

