from rest_framework import generics
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializers, MessageSerializersPOST

@api_view(['GET','POST'])
def message_list(request, x, format=None):
    if request.method=='GET':
        messages=Message.objects.all().order_by('-updatedate')
        messages=messages[10*x:10*(x+1)]
        serializer=MessageSerializers(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MessageSerializersPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def message_detail(request, pk):
    try:
        message = Message.objects.get(pk=pk)
    except RuntimeError:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MessageSerializers(message)
        return Response(serializer.data)
# Create your views here.
