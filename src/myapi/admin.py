from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.db.models import Prefetch
from django import forms
from django.db import models
import datetime

from .models import Products
from .models import OrderDetails
from .models import Orders

#Unregister default fields
admin.site.unregister(User)
admin.site.unregister(Group)


#class created to validate inline objects, in this case - Products
class OrderDetailsInlineFormSet(forms.models.BaseInlineFormSet):
    def save_new(self, form, commit=True):
        saved_instances = super(OrderDetailsInlineFormSet, self).save_new(form, commit=False)
        if commit:
            saved_instances.productid.unitsinstock -= saved_instances.quantity
            saved_instances.productid.save()
            saved_instances.save()
        return saved_instances
    #def save_existing(self, commit=True):
    #    saved_instances = super(OrderDetailsInlineFormSet, self).save_existing(form, commit=False)
    #    if commit:
    #        saved_instances.save()
    #    return saved_instances
    def clean(self):
        setOfProducts = set()
        if(self.is_valid()):
            for productForm in self.cleaned_data:
                reservedQuantity = productForm.get('quantity')
                product = productForm.get('productid')
                unitsInStock = product.unitsinstock
                price = productForm.get('unitprice')
                discount = productForm.get('discount')
                #check if the same product was not chosen twice
                if product in setOfProducts:
                    raise forms.ValidationError("Product " + str(product) + " was added more than once!")
                else:
                    setOfProducts.add(product)
                #check if unitprice is greater than 0
                if price <= 0:
                    raise forms.ValidationError("Unitprice for product " + str(product) + " has to be greater than 0!")
                #check if discount is between 0 and 1
                if discount < 0 or discount > 1:
                    raise forms.ValidationError("Discount for product " + str(product) + " has to be value between 0 and 1!")
                #check product quantity availability
                if reservedQuantity > unitsInStock:
                    raise forms.ValidationError("Maximum quantity for product " + str(product) + " is " + str(unitsInStock) + "!")


#representation of orderdetails inline, used in Products and Orders
class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails
    formset = OrderDetailsInlineFormSet
    extra = 0
    can_delete = True


#class created to validate main object being created - Order
class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
    def clean(self):
        orderDate = self.cleaned_data.get('orderdate')
        requiredDate = self.cleaned_data.get('requireddate')
        #order date validation
        if orderDate >= (requiredDate - datetime.timedelta(days=1)):
            raise forms.ValidationError("Orderdate must be at least 24 hours before Required date!")
        return self.cleaned_data


#class created to create Orders view with Products Inline
class OrdersAdmin(admin.ModelAdmin):
    form = OrdersForm
    inlines = (OrderDetailsInline, )
    fieldsets = [
        (None, {'fields': ['customerid', 'employeeid', 'orderdate', 'requireddate', 'shippeddate', 'shipvia', 'freight', 'shipname', 'shipaddress', 'shipcity', 'shipregion', 'shippostalcode', 'shipcountry', ]}),
        ('Order Summary', {'fields': ['summary', ]}),
    ]
    readonly_fields = ('summary', )

admin.site.register(Orders, OrdersAdmin)


#class created to create Product view with Orders Inline
class ProductsAdmin(admin.ModelAdmin):
    inlines = (OrderDetailsInline, )

admin.site.register(Products, ProductsAdmin)

##################################
### custorm reports start here ###
##################################

#proxy class
class OrdersProxy(Orders):
    class Meta:
        verbose_name_plural = 'Orders Reports'
        proxy = True

class OrdersProxyAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        pref = Prefetch('orderdetailsFK', \
            Products.objects.select_related('categoryid', 'supplierid') \
                .only('productid', 'productname', 'categoryid', 'categoryid__categoryname', 'supplierid', 'supplierid__companyname'), to_attr='prod')
        return super(OrdersProxyAdmin, self).get_queryset(request) \
            .select_related('customerid') \
            .prefetch_related(pref) \
            .only('orderid', 'orderdate', 'customerid', 'customerid__companyname', 'orderdetailsFK__productid', 'orderdetailsFK__productname', \
                'orderdetailsFK__supplierid', 'orderdetailsFK__supplierid__companyname', 'orderdetailsFK__categoryid', 'orderdetailsFK__categoryid__categoryname')

    def getorderid(self, obj):
        return obj.orderid

    def getcustomerid(self, obj):
        return obj.customerid

    def getorderdate(self, obj):
        return obj.orderdate

    def getproducts(self, obj):
        return ", ".join([p.productname for p in obj.prod])

    def getcategories(self, obj):
        return ", ".join([c for c in set([p.categoryid.categoryname for p in obj.prod])])

    def getsuppliers(self, obj):
        return ", ".join([s for s in set([p.supplierid.companyname for p in obj.prod])])

    list_per_page = 10
    list_display = ('getorderid', 'getcustomerid', 'getorderdate', 'getproducts', 'getcategories', 'getsuppliers')
    list_filter = ("orderdetailsFK__categoryid", "orderdetailsFK__supplierid")

admin.site.register(OrdersProxy, OrdersProxyAdmin)
