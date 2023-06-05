from django.shortcuts import render
from rest_framework import viewsets

from .models import Friend, Borrowed, Belonging, Newclient
from .serializer import FriendSerializer, BelongingSerializer, BorrowedSerializer, NewClientSerializer



class NewClientViewset(viewsets.ModelViewSet):
    queryset = Newclient.objects.all()
    serializer_class = NewClientSerializer


class FriendViewset(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class BelongingViewset(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer


class BorrowedViewset(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer

