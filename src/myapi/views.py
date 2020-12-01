#from django.shortcuts import render
#from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


from .serializers import CategoriesSerializer
#from .serializers import ProductsSerializer
#from .serializers import SuppliersSerializer

from .models import Categories
from .models import Products
from .models import Suppliers
# Create your views here.

class CategoriesView(APIView):
    def get(self,request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many = True)
        return Response({"Categories":serializer.data})

    def post(self, request):
        category = request.data.get('category')

        # Create an article from the above data
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
