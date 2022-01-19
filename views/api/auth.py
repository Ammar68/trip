from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import SignupSerializer
from django.contrib.auth.models import User

class signup(CreateAPIView):
    serializer_class = SignupSerializer
    

class login(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SignupSerializer
    

