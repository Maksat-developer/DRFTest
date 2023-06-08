from django.urls import path
from .views import user_create_view


urlpatterns = [
    path('register/', user_create_view, name='register'),
]

