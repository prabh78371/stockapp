from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('stockapi/',views.stock_api,name="stockApi"),
    path('stockapi/<int:product_id>',views.stock_api,name="stockApi"),
    path('productapi/',views.product_api,name="productApi"),
 


]