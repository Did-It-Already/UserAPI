from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from .serializer import UserSerializer
from .models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = UserSerializer

