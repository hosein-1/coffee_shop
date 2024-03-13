from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/products.html'
    context_object_name = 'products'
