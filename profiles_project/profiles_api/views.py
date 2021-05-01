from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers, models, permissions

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

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a hello message"""
        a_viewset = [
            'list, create, retrieve, update, partial_update',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by Its ID"""
        return Response({"http method": "GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Removing an object"""
        return Response({'http method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and Updating Profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')