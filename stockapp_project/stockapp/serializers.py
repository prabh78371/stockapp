from dataclasses import field, fields
from pyexpat import model
from .models import Product,Inventory,Category,Transaction
from rest_framework import serializers

class Productserilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
       
class categoryserilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 1

class Inventoryserilizer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
        depth = 2

class Transactionserilizer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        depth = 3