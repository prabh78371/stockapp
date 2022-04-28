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

@api_view(['GET'])
def Products(request,barcode_number=None):
    if request.method ==  'GET':
        id = barcode_number
        if id is not None:
            prod = Product.objects.get(barcode_number=id)
            serilizer = Productserilizer(prod)
            return Response(serilizer.data)
        prod = Product.objects.all()
        serilizer = Productserilizer(prod,many=True,)
        return Response(serilizer.data)
