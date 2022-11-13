from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .serializers import*
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
from django.http import HttpResponseGone,JsonResponse
import jwt,datetime
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
from rest_framework import status
from django.http import Http404
from utilisateur.models import*
from utilisateur.serializers import*
#Liste des dons détailler ou non par general
class ListDonateurd(generics.RetrieveUpdateDestroyAPIView):
    queryset=DonateurUser.objects.all()
    permission_classes=[AllowAny]
    serializer_class=DonateurOrSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["organisations","user_name"]
    filterset_fields=["organisations","user_name"]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        pagine=self.paginate_queryset(queryset)
        serializer = DonateurOrSerializer(queryset, many=True)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data})

class ListDonateur(generics.ListAPIView):
    queryset=DonateurUser.objects.all()
    permission_classes=[AllowAny]
    serializer_class=DonateurOrSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["organisations","user_name"]
    filterset_fields=["organisations","user_name"]


class ListDonArgeda(APIView):
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["organisations","user_name"]
    filterset_fields=["organisations","user_name"]
    def get_object(self, pk):
        try:
            user = self.request.user
            return EffectuerDonArge.objects.get(pk=pk)
        except EffectuerDonArge.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EffectuerArgSerializer(snippet)
        return Response({'data':serializer.data,'status':status.HTTP_200_OK})
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EffectuerArgSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':status.HTTP_200_OK,'message':'votre dons est bien parvenu'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({'status':status.HTTP_204_NO_CONTEN,'message':'suppression reussi'})

class ListDonArgea(generics.ListAPIView):
    model=EffectuerDonArge
    permission_classes=[AllowAny]
    serializer_class=EffectuerArgSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["donateur","typeDons","categorieV","cibleV","provider"]
    filterset_fields=["donateur","typeDons","categorieV","cibleV","provider"]
    def get_queryset(self):
        user = self.request.user
        return EffectuerDonArge.objects.all()

class ListDonNaturedad(APIView):
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["donateur","typeDons","categorieV","cibleV","provider"]
    filterset_fields=["donateur","typeDons","categorieV","cibleV","provider"]
    def get_object(self, pk):
        try:
            return EffectuerDonNature.objects.get(pk=pk)
        except EffectuerDonNature.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EffectuerNatSerializer(snippet)
        return Response({'data':serializer.data,'status':status.HTTP_200_OK})
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EffectuerNatSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':status.HTTP_200_OK,'message':'votre dons est bien parvenu'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({'status':status.HTTP_204_NO_CONTEN,'message':'suppression reussi'})

class ListDonNaturea(generics.ListAPIView):
    model=EffectuerDonNature
    permission_classes=[AllowAny]
    serializer_class=EffectuerNatSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["donateur","typeDons","categorieV","cibleV"]
    filterset_fields=["donateur","typeDons","categorieV","cibleV"]
    def get_queryset(self):
        user = self.request.user
        return EffectuerDonNature.objects.all()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


