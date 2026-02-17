from .models import User
from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'password']
        extra_kwargs = {
            'password': {'write_only': True} # Hidden in GET responses for security
        }

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user


# Our views
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer