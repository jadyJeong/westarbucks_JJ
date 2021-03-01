# this is the main urls.py for project.

from django.urls import path, include


urlpatterns = [
    path("products", include("products.urls"))
    ]