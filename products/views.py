from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import Response,serializers,status
from drf_spectacular.utils import extend_schema
from .serializer import ProductSerializer
from .models import ProductModel
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@extend_schema(request=ProductSerializer)
@api_view(['POST'])
def addProduct(request):
    if not request.user.is_authenticated:
        return Response({
            'message': 'Authentication required',
            'status': status.HTTP_401_UNAUTHORIZED
        })
    serializer = ProductSerializer(data=request.data)
    if serializer.validate():
        last_pid = ProductModel.objects.filter('pid').last()
        if last_pid:
            id = int(last_pid[4:])
            new_pid = id +1
            pid = f'VMPD{new_pid:05}'
            serializer.save(pid=pid)
        else:
            new_pid=1
            pid = f'VMPD{new_pid:05}'
            serializer.save(pid=pid)
        return Response({
            'message':'product created successfully',
            'status':status.HTTP_200_OK
        })
    else:
        return({
            'message':'failed to create',
            'error': serializer.error_messages,
            'status': status.HTTP_400_BAD_REQUEST

        })


        


