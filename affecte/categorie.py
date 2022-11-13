from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .serializers import*
from .models import *
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
from django.http import HttpResponseGone,JsonResponse
import jwt,datetime
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
from rest_framework import status
from django.http import Http404


class CategorieO(generics.RetrieveUpdateDestroyAPIView):
    queryset=Categorie_obj.objects.all()
    permission_classes=[AllowAny]
    serializer_class=CateObjetSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        message='success'
        queryset = self.get_queryset()
        serializer = CateObjetSerializer(queryset, many=True)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data,'message':message})

class ListCategorieO(generics.ListCreateAPIView):
    queryset=Categorie_obj.objects.all()
    permission_classes=[AllowAny]
    serializer_class=CateObjetSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        message='success'
        queryset = self.get_queryset()
        serializer = CateObjetSerializer(queryset, many=True)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data,'message':message})


class CategorieVulnerable(generics.RetrieveUpdateDestroyAPIView):
    queryset=Vulnerable_categorie.objects.all()
    permission_classes=[AllowAny]
    serializer_class=VulnerableCateSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        message='success'
        queryset = self.get_queryset()
        pagine=self.paginate_queryset(queryset)
        serializer = VulnerableCateSerializer(queryset, many=True)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data,'message':message})

class ListCategorieVulnerable(generics.ListCreateAPIView):
    queryset=Vulnerable_categorie.objects.all()
    permission_classes=[AllowAny]
    serializer_class=VulnerableCateSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        message='success'
        queryset = self.get_queryset()
        pagine=self.paginate_queryset(queryset)
        serializer = VulnerableCateSerializer(queryset, many=True)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data,'message':message})