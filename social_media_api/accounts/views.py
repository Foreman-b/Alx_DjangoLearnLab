from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

# Now Let create Registration view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Let create a token for new user here
        token = Token.objects.get(user=user)

        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


# Let create Login view, let use ObtainAuthToke to check for user username/password automatically

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })
    
   
    
# Let handle user profile
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer = UserSerializer
    permission_classes = [IsAuthenticated]

    
    def get_object(self):
        return self.request.user

