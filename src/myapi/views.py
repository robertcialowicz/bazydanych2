from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CategoriesSerializer
from .serializers import ProductsSerializer
from .serializers import SuppliersSerializer

from .models import Categories
from .models import Products
from .models import Suppliers
# Create your views here.

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('categoryid')
    serializer_class = CategoriesSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('productid')
    serializer_class = ProductsSerializer

class SuppliersViewSet(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all().order_by('supplierid')
    serializer_class = SuppliersSerializer
