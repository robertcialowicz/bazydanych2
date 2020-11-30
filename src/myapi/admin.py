from django.contrib import admin
from .models import Categories
from .models import Products
from .models import Suppliers
# Register your models here.
admin.site.register(Suppliers)
admin.site.register(Products)
admin.site.register(Categories)