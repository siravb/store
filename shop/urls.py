from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductsList.as_view(), name="product_all"),
    path("product/<str:slug>/", views.ProductDetail.as_view(), name="product-detail"),
]