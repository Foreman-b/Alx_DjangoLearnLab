from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser



class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]


    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    


class CustomUserManager(BaseUserManager):
    # Let create and save User with given email, DOB and password
    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have a valid email address")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
       extra_fields.setdefault('is_staff', True)
       extra_fields.setdefault('is_superuser', True)

       return self.create_user(username, email, date_of_birth, password, **extra_fields)



class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='upload/profile_photo', null=True, blank=True)

    REQUIRED_FIELDS = ['date_of_birth', 'email']

    objects = CustomUserManager()