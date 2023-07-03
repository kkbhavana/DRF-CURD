from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer


# Create your views here.
@api_view(['Get'])
def api_overview(request):
    api_urls = {
        "list": '/product/list',
        "Details": '/product/details/<int:id>',
        "Create": '/product/create',
        "Delete": '/product/delete/<int:id>',
        "Update": "/product/update/<int:id>",
    }
    return Response(api_urls)


# list
@api_view(['Get'])
def showall(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# create
@api_view(['Post'])
def createproduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# detail
@api_view(['Get'])
def detailview(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


# update
@api_view(['Post'])
def updateview(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=products, data=request.data, )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# delete
@api_view(['Delete'])
def deleteview(request, pk):
    products = Product.objects.get(id=pk)
    products.delete()
    return Response('Item Deleted Successfully')
