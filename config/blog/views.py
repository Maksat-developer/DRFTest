from django.shortcuts import render
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer
from rest_framework import generics




class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

category_list_create = CategoryListCreate.as_view()


class CategoryDestroy(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

category_delete = CategoryDestroy.as_view()


class CategoryUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

category_update = CategoryUpdate.as_view()


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_create = ProductListCreate.as_view()



class ProductDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_delete = ProductDestroy.as_view()


class ProductUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_update = ProductUpdate.as_view()


