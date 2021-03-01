from django.urls import path, include
from products.views import ProductsView


urlpatterns = [

    path('', ProductsView.as_view())

    ]