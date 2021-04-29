from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'GET, PUT, PATCH, DELETE, POST',
            'Only 4 requests are popular tbh',
            'Django is pretty cool'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello Message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'Put'})

    def patch(self, request, pk=None):
        """Handle a partial update for an object"""
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        """Deletes a request object"""
        return Response({'method': 'Delete'})