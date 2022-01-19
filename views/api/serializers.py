from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class SignupSerializer(ModelSerializer):
    model = User
    fields = ['email', 'name', 'password']
    
class LoginSerializer(ModelSerializer):
    model = User
    fields = ['email', 'password']
    