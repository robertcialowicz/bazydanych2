from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Products
from .models import OrderDetails
from .models import Orders

#Unregister default fields
admin.site.unregister(User)
admin.site.unregister(Group)

class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails
    extra = 0

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    inlines = (OrderDetailsInline, )

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    inlines = (OrderDetailsInline, )
    #ordering = ('requireddate',)
