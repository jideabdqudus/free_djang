from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API view"""
    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'GET, PUT, PATCH, DELETE, POST',
            'Only 4 requests are popular tbh',
            'Django is pretty cool'
        ]
