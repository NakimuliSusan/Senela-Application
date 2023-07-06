from django.shortcuts import render
from Product.serializers import ProductSerializer
from rest_framework.decorators import api_view
from Product.models import Product
from rest_framework import status
from rest_framework.response import Response




# Create your views here.

@api_view(['GET', 'POST'])
def product_list(request):
    """
    Creates and retrieves all products from the database
    """
    if request.method == 'GET':
        """
        Retrieves all products
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        """
        Creates a new product and saves it to the database
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    """
    Retrieve, update and delete a product
    """
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        """
        Retrieves a single product based on id
        """
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        """
        Updates a product
        """
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        """
        Deletes a product
        """
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
