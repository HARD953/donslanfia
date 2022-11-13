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


class TypeOjet(generics.RetrieveUpdateDestroyAPIView):
    queryset=Type_obj.objects.all()
    permission_classes=[AllowAny]
    serializer_class=TypeObjetSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        message='success'
        queryset = self.get_queryset()
        pagine=self.paginate_queryset(queryset)
        serializer = TypeObjetSerializer(queryset, many=True)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data,'message':message})

class ListTypeOjet(generics.ListCreateAPIView):
    queryset=Type_obj.objects.all()
    permission_classes=[AllowAny]
    serializer_class=TypeObjetSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["categorie_objet"]
    filterset_fields=["categorie_objet"]
    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     message='success'
    #     queryset = self.get_queryset()
    #     serializer = TypeObjetSerializer(queryset, many=True)
    #     return Response({'status':status.HTTP_200_OK,'data':serializer.data,'message':message})

class TypeVulnerable(generics.RetrieveUpdateDestroyAPIView):
    queryset=Vulnerable_cible.objects.all()
    permission_classes=[AllowAny]
    serializer_class=VulnerableCibSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        message='success'
        queryset = self.get_queryset()
        pagine=self.paginate_queryset(queryset)
        serializer = VulnerableCibSerializer(queryset, many=True)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data,'message':message})

class ListTypeVulnerable(generics.ListCreateAPIView):
    queryset=Vulnerable_cible.objects.all()
    permission_classes=[AllowAny]
    serializer_class=VulnerableCibSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["categorie_vulnerable"]
    filterset_fields=["categorie_vulnerable"]
    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     message='success'
    #     queryset = self.get_queryset()
    #     pagine=self.paginate_queryset(queryset)
    #     serializer = VulnerableCateSerializer(queryset, many=True)
    #     return Response({'status':status.HTTP_200_OK,'data':serializer.data,'message':message})