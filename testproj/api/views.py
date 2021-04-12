from rest_framework import generics
from .models import Message
from .serializers import MessageSerializers
from .pagination import CustomPagination
from django.shortcuts import render

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('-publicatedate')
    serializer_class = MessageSerializers
    pagination_class = CustomPagination
    
    

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers