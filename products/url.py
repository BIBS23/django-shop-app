from django.urls import path
from .views import addProduct

url_patterns = [path('api/add_products',addProduct)]