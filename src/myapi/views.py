#from django.shortcuts import render
#from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .serializers import CategoriesSerializer
from .serializers import ProductsSerializer
from .serializers import SuppliersSerializer

from .models import Categories
from .models import Products
from .models import Suppliers
# Create your views here.

class CategoriesView(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            category = get_object_or_404(Categories.objects.all(), pk=pk)
            serializer = CategoriesSerializer(category, many = False)
            return Response({"Categories":serializer.data})
        else:
            categories = Categories.objects.all()
            serializer = CategoriesSerializer(categories, many = True)
            return Response({"Categories":serializer.data})

    def post(self, request):
        category = request.data.get('category')

        # Create a category from the above data
        serializer = CategoriesSerializer(data=category)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"success": "category '{}' created successfully".format(category_saved.categoryname)})

    def update(self, instance, validated_data):
        instance.categoryname = validated_data.get('categoryname', instance.categoryname)
        instance.description = validated_data.get('description', instance.description)
        instance.categoryid = validated_data.get('categoryid', instance.categoryid)
        instance.picture = validated_data.get('picture', instance.picture)

        instance.save()
        return instance

    def put(self, request, pk):
        saved_category = get_object_or_404(Categories.objects.all(), pk=pk)
        data = request.data.get('category')
        serializer = CategoriesSerializer(instance=saved_category, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"success": "Category '{}' updated successfully".format(category_saved.categoryname)})

    def delete(self, request, pk):
    # Get object with this pk
        category = get_object_or_404(Categories.objects.all(), pk=pk)
        category.delete()
        return Response({"message": "category with id `{}` has been deleted.".format(pk)},status=204)

class SuppliersView(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            supplier = get_object_or_404(Suppliers.objects.all(), pk=pk)
            serializer = SuppliersSerializer(supplier, many = False)
            return Response({"Supplier":serializer.data})
        else:
            suppliers = Suppliers.objects.all()
            serializer = SuppliersSerializer(suppliers, many = True)
            return Response({"Suppliers":serializer.data})

    def post(self, request):
        supplier = request.data.get('supplier')

        # Create a supplier from the above data
        serializer = SuppliersSerializer(data=supplier)
        if serializer.is_valid(raise_exception=True):
            supplier_saved = serializer.save()
        return Response({"success": "supplier '{}' created successfully".format(supplier_saved.companyname)})

    def update(self, instance, validated_data):
        instance.supplierid = validated_data.get('suppllierid', instance.supplierid)
        instance.companyname = validated_data.get('companyname', instance.companyname)
        instance.contactname = validated_data.get('contactname', instance.contactname)
        instance.contacttitle = validated_data.get('contacttitle', instance.contacttitle)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.region = validated_data.get('region', instance.region)
        instance.postalcode = validated_data.get('postalcode', instance.postalcode)
        instance.country = validated_data.get('country', instance.country)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.fax = validated_data.get('fax', instance.fax)
        instance.homepage = validated_data.get('homepage', instance.homepage)

        instance.save()
        return instance

    def put(self, request, pk):
        saved_supplier= get_object_or_404(Suppliers.objects.all(), pk=pk)
        data = request.data.get('supplier')
        serializer = SuppliersSerializer(instance=saved_supplier, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            supplier_saved = serializer.save()
        return Response({"success": "Supplier '{}' updated successfully".format(supplier_saved.companyname)})

    def delete(self, request, pk):
    # Get object with this pk
        supplier = get_object_or_404(Suppliers.objects.all(), pk=pk)
        supplier.delete()
        return Response({"message": "supplier with id `{}` has been deleted.".format(pk)},status=204)


class ProductsView(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            product = get_object_or_404(Products.objects.all(), pk=pk)
            serializer = ProductsSerializer(product, many = False)
            return Response({"Product":serializer.data})
        else:
            products = Products.objects.all()
            serializer = ProductsSerializer(products, many = True)
            return Response({"Products":serializer.data})

    def post(self, request):
        product = request.data.get('product')
        supplier = get_object_or_404(Suppliers, supplierid=product.get('supplierid'))
        category = get_object_or_404(Categories, categoryid=product.get('categoryid'))

        # Create a supplier from the above data
        serializer = ProductsSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save(categoryid=category, supplierid=supplier)
        return Response({"success": "product '{}' created successfully".format(product_saved.productname)})

    def update(self, instance, validated_data):
        instance.productid = validated_data.get('productid', instance.productid)
        instance.productname = validated_data.get('productname', instance.productname)
        instance.supplierid = validated_data.get('supplierid', instance.supplierid)
        instance.categoryid = validated_data.get('categoryid', instance.categoryid)
        instance.quantityperunit = validated_data.get('quantityperunit', instance.quantityperunit)
        instance.unitprice = validated_data.get('unitprice', instance.unitprice)
        instance.unitsinstock = validated_data.get('unitsinstock', instance.unitsinstock)
        instance.unitsonorder = validated_data.get('unitsonorder', instance.unitsonorder)
        instance.reorderlevel = validated_data.get('reorderlevel', instance.reorderlevel)
        instance.discontinued = validated_data.get('discontinued', instance.discontinued)

        instance.save()
        return instance

    def put(self, request, pk):
        saved_product= get_object_or_404(Products.objects.all(), pk=pk)
        data = request.data.get('product')
        serializer = ProductsSerializer(instance=saved_product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"success": "Product '{}' updated successfully".format(product_saved.productname)})

    def delete(self, request, pk):
    # Get object with this pk
        product = get_object_or_404(Products.objects.all(), pk=pk)
        product.delete()
        return Response({"message": "product with id `{}` has been deleted.".format(pk)},status=204)
