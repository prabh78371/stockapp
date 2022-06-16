from dataclasses import field, fields
from pyexpat import model
from .models import Product,Inventory,Category,Transaction
from rest_framework import serializers
       
class categoryserilizer(serializers.ModelSerializer):
    # product = serializers.HiddenField(default = 1)
    class Meta:
        model = Category
        fields = ['product','product_code','packs_per_carton']
        depth = 1
        
class Productserilizer(serializers.ModelSerializer):
    barcode_number = serializers.HiddenField(default = 1)
    category_set = Categoryserilizer(many=True,read_only=True)
    class Meta:
        model = Product
        ffields = ['barcode_number','name','category_set']

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
