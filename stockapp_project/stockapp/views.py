from functools import partial
from itertools import product
from urllib import response
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Productserilizer,Transactionserilizer,categoryserilizer,Inventoryserilizer
from .models import Category, Product,Transaction,Inventory
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def stock_api(request,product_id=None):
    if request.method ==  'GET':
        id=product_id
        if id is not None:
            prod = Inventory.objects.get(product_id=id)
            serilizer = Inventoryserilizer(prod)
            return Response(serilizer.data)
        prod = Inventory.objects.all()
        serilizer = Inventoryserilizer(prod,many=True)
        return Response(serilizer.data)

    if request.method == 'POST':
        serilizer = Category(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)

    

@api_view(['GET','POST'])
def product_api(request,pk=None):
    if request.method ==  'GET':
        id = pk
        if id is not None:
            prod = Transaction.objects.get(id=id)
            serilizer = Transactionserilizer(prod)
            return Response(serilizer.data)
        prod = Transaction.objects.all()
        serilizer = Transactionserilizer(prod,many=True)
        return Response(serilizer.data)

    if request.method == 'POST':
        serilizer = Transactionserilizer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)