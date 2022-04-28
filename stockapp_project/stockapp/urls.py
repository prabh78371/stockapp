from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Products/',views.Products,name="productapi"),
    path('Products/<int:barcode_number>',views.Products,name="productapi"),
 


]
