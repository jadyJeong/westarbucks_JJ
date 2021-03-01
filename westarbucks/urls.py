# this is the main urls.py for project.
from django.urls import path, include
from products import urls


urlpatterns = [

    path("products", include("products.urls"))

    ]