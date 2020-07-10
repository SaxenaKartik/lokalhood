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

    def list(self, request):
        queryset = models.UserProfile.objects.all()
        phone = request.query_params.get('phone', None)
        if phone is not None:
            phone = "+91" + phone
            queryset = queryset.filter(phone_no = phone)
        serializer = serializers.UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)

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

    def list(self, request):
        queryset = models.Request.objects.all()
        rid = request.query_params.get('rid', None)
        user = request.query_params.get('user', None)
        shop = request.query_params.get('shop', None)
        if rid is not None:
            queryset = queryset.filter(id = rid)
        if user is not None:
            queryset = queryset.filter(user = user)
        if shop=="null":
            queryset = queryset.filter(shop = None)
        elif shop is not None:
            queryset = queryset.filter(shop = shop)
        serializer = serializers.RequestSerializer(queryset, many=True)
        return Response(serializer.data)


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
