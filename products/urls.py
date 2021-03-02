from django.urls import path, include
from products.views import ProductView, CategoryView


urlpatterns = [

    path('/product', ProductView.as_view()),
    path('/category', CategoryView.as_view())

    ]