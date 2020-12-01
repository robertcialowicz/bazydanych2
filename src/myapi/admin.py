from django.contrib import admin
from .models import Categories
from .models import Products
from .models import Suppliers
from .models import Customercustomerdemo
from .models import CustomerDemographics
from .models import Customers
from .models import Employeeterritories
from .models import Region
from .models import Territories
from .models import Employees
from .models import OrderDetails
from .models import Orders
from .models import Shippers
# Register your models here.
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Suppliers)
admin.site.register(Customercustomerdemo)
admin.site.register(CustomerDemographics)
admin.site.register(Customers)
admin.site.register(Employeeterritories)
admin.site.register(Region)
admin.site.register(Territories)
admin.site.register(Employees)
admin.site.register(OrderDetails)
admin.site.register(Orders)
admin.site.register(Shippers)
