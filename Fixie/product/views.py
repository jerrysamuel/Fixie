from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductSerializer
from .models import products


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = products.objects.all()
    
# Create your views here.
