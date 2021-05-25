from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import RegisterSerilazer, MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics, serializers


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes =(AllowAny,)
    serializer_class = MyTokenObtainPairSerializer



# registraton view for registring user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerilazer