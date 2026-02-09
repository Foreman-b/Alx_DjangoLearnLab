from django.db import models
from django.conf import settings


class Post(models.Model):
    # This is a model representing blog post 
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    #Let link to Django User model
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='posts'
        )

    def __str__(self):
        # String representation of the Post object in Admin
        return self.title
