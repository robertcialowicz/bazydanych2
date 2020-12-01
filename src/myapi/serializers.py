# serializers.py
from rest_framework import serializers

from .models import Categories
from .models import Products
from .models import Suppliers

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('categoryid', 'categoryname', 'description', 'picture')

        def create(self, validated_data):
            return Categories.objects.create(**validated_data)

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    supplierid = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    categoryid = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Products
        fields = ('productid','productname','supplierid','categoryid','quantityperunit','unitprice','unitsinstock','unitsonorder','reorderlevel','discontinued')
        
        def create(self, validated_data):
            return Products.objects.create(**validated_data)


class SuppliersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Suppliers
        fields = ('supplierid','companyname','contactname','contacttitle','address','city','region','postalcode','country','phone','fax','homepage')
        def create(self, validated_data):
            return Suppliers.objects.create(**validated_data)

