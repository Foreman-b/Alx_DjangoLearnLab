from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    # Let converts Book model instances into JSON format.
    class Meta:
        model = Book
        fields = '__all__'
        
    # Now, let make sure the publication year is not in the future
    def validate_publication_year(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    

# Let convert Author model instance into JSON format.
class AuthorSerializer(serializers.ModelSerializer):
    # The 'books field here works because of the 'related_name' in models.py
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']