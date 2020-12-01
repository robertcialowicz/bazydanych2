# myapi/urls.py

from django.urls import include, path
#from rest_framework import routers
#from . import views

from .views import CategoriesView


app_name = "myapi"

#router = routers.DefaultRouter()
#router.register(r'Categories', views.CategoriesViewSet)
#router.register(r'Products', views.ProductsViewSet)
#router.register(r'Suppliers', views.SuppliersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('Categories/', CategoriesView.as_view()),
    path('Categories/<int:pk>', CategoriesView.as_view())
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
