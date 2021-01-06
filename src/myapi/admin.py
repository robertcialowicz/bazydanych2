from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django import forms

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
    def save_existing(self, commit=True):
        saved_instances = super(OrderDetailsInlineFormSet, self).save_existing(form, commit=False)
        if commit:
            saved_instances.save()
        return saved_instances
    def clean(self):
        for productForm in self.cleaned_data:
            reservedQuantity = productForm.get('quantity')
            product = productForm.get('productid')
            unitsInStock = product.unitsinstock
            price = productForm.get('unitprice')
            discount = productForm.get('discount')
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


#class created to validate main object being created - Order
class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
    def clean(self):
        orderDate = self.cleaned_data.get('orderdate')
        requiredDate = self.cleaned_data.get('requireddate')
        #order date validation
        if orderDate >= requiredDate:
            raise forms.ValidationError("Requirred date cannot be before Orderdate!")
        return self.cleaned_data


#class created to create Orders view with Products Inline
class OrdersAdmin(admin.ModelAdmin):
    form = OrdersForm
    inlines = (OrderDetailsInline, )

admin.site.register(Orders, OrdersAdmin)


#class created to create Product view with Orders Inline
class ProductsAdmin(admin.ModelAdmin):
    inlines = (OrderDetailsInline, )

admin.site.register(Products, ProductsAdmin)
