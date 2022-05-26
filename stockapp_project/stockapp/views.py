from functools import partial
from itertools import product
from urllib import response
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Productserilizer,Transactionserilizer,Categoryserilizer,Inventoryserilizer
from .models import Category, Product,Transaction,Inventory
from rest_framework import status

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def products(request,barcode_number=None):
    if request.method ==  'GET':
        id = barcode_number
        if id is not None:
            prod = Product.objects.get(barcode_number=id)
            serilizer = Productserilizer(prod)
            return Response(serilizer.data)
        prod = Product.objects.all()
        serilizer = Productserilizer(prod,many=True,)
        return Response(serilizer.data,status = status.HTTP_200_OK)

    
    if request.method == 'POST':
        serilizer = Productserilizer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = barcode_number
        prod = Product.objects.get(barcode_number=id)
        serilizer = Productserilizer(prod,data = request.data )
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)  

    if request.method == 'PATCH':
        id = barcode_number
        prod = Product.objects.get(barcode_number=id)
        serilizer = Productserilizer(prod,data = request.data,partial =True )
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)  

    if request.method == 'DELETE':
        id = barcode_number
        prod = Product.objects.get(barcode_number=id)
        prod.delete()
        return Response({})

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def category(request,pk=None):
    if request.method ==  'GET':
        id = pk
        if id is not None:
            cat = Category.objects.get(id=id)
            serilizer = Categoryserilizer(cat)
            return Response(serilizer.data)
        cat = Category.objects.all()
        serilizer = Categoryserilizer(cat,many=True,)
        return Response(serilizer.data)
  
    if request.method == 'POST':
        serilizer = Categoryserilizer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        cat = Category.objects.get(id=id)
        serilizer = Categoryserilizer(cat,data = request.data )
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)  

    if request.method == 'PATCH':
        id = pk
        cat = Category.objects.get(id=id)
        serilizer = Categoryserilizer(cat,data = request.data,partial =True )
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)  

    if request.method == 'DELETE':
        id = pk
        prod = Category.objects.get(id=id)
        prod.delete()
        return Response({})

@api_view(['GET'])
def inventory(request):
    if request.method ==  'GET':
        prod = Inventory.objects.all()
        serilizer = Inventoryserilizer(prod,many=True,)
        return Response(serilizer.data)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def transaction(request,pk=None):
    if request.method ==  'GET':
        id = pk
        if id is not None:
            trans = Transaction.objects.get(id=id)
            serilizer = Transactionserilizer(trans)
            return Response(serilizer.data)
        cat = Transaction.objects.all()
        serilizer = Transactionserilizer(cat,many=True,status = status.HTTP_200_OK)
        return Response(serilizer.data,status = status.HTTP_400_BAD_REQUEST)
  
    if request.method == 'POST':
        serilizer = Transactionserilizer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)
