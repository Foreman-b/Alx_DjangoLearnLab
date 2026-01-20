from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import User


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')



class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Now let display controls the columns shows in the user list view
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']



# Now let register the models with the custom admin class
admin.site.register(User, CustomUserAdmin)


admin.site.register(Book, BookAdmin)
