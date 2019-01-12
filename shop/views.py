from django.shortcuts import render
from django.views.generic import ListView, View

from .models import Product


class ProductsList(ListView):
    """Список всех продуктов"""
    model = Product
    template_name = "shop/list-product.html"



class ProductDetail(View):
    def get (self, request, slug):
        product = Product.objects.get(slug__exact=slug)
        return render(request, "shop/detail-product.html", context={'product': product})