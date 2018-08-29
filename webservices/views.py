from django.shortcuts import render
from users.models import *
from .serializer import *
from rest_framework import viewsets

# Create your views here.
class producto_viewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = producto_serializer

class user_viewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_serializer
'''
class categoria_viewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = categoria_serializer'''
