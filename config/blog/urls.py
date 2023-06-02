from django.urls import path
from .views import *


urlpatterns = [
    path('product-list-create/', product_list_create, name='product-list-create'),
    path('product-delete/<int:pk>/', product_delete, name='product-delete'),
    path('product-update/<int:pk>/', product_update, name='product-update'),

    path('category-list-create/', category_list_create, name='category_list_create'),
    path('category-delete/<int:pk>/', category_delete, name='category-delete'),
    path('category-update/<int:pk>/', category_update, name='category-update'),
]
