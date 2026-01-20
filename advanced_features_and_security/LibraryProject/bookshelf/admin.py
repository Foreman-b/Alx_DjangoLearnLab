from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile
from .models import User, CustomUserAdmin




admin.site.register([Author, Book, Library, Librarian])
admin.site.register(UserProfile)

# Now let register the models with the custom admin class
admin.site.register(User, CustomUserAdmin)

