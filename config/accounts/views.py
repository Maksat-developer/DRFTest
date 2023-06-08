from django.shortcuts import render

from .models import User
from .serializer import UserSerializer

from rest_framework.response import Response
from rest_framework import status

from django.views import UserViewSet as DjoserUserViewSet


class UserCreateView(DjoserUserViewSet):
    serializer_class = UserSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
user_create_view = UserCreateView.as_view({'post':'create'})
