from dataclasses import field, fields
from pyexpat import model
from .models import Product,Inventory,Category,Transaction
from rest_framework import serializers
       
class categoryserilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['product_code','packs_per_carton']
        depth = 1
        
class Productserilizer(serializers.ModelSerializer):
    category_set = Categoryserilizer(many=True,read_only=True)
    class Meta:
        model = Product
        ffields = ['name','category_set']

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
