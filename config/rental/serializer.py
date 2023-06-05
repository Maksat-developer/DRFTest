from rest_framework import serializers
from .models import Friend, Belonging, Borrowed, Newclient

class NewClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newclient
        fields = ('id', 'client', 'is_new')
        

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'name')


class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Belonging
        fields = ('id', 'name')


class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowed
        fields = ('id', 'what', 'to_who', 'client', 'created_at', 'returned')
