from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from lokalhood_api import models
from lokalhood_api import serializers
from rest_framework.authentication import TokenAuthentication
from lokalhood_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating users"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('id', 'name', 'email', 'phone_no',)

class ShopViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating shops"""

    serializer_class = serializers.ShopSerializer
    queryset = models.Shop.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('id', 'name', 'category', 'locality',)


class RequestViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating requests"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.RequestSerializer
    queryset = models.Request.objects.all()
    permission_classes = (permissions.UpdateOwnRequest,IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('id', 'deliver_addr', 'items' ,)

    def perform_create(self, serializer):
        """ Sets the logged in user as the requesting user"""
        serializer.save(user = self.request.user)

class UserLoginAPIView(ObtainAuthToken):
    """ Handle creating user auth token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    # since ObtainAuthToken class doesn't have renderer_classes defined
