from re import template
from unicodedata import name
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
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
from rest_framework import status
from django.http import Http404
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.template.loader import render_to_string
# from django.http import HttpResponse
# from django.core.mail import send_mail

# def success(request):
#     subject = "Greetings from Programink"  
#     msg     = "Learn Django at Programink.com"  
#     to      = request.data['email']  
#     res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to],fail_silently=False)  
#     if(res == 1):  
#         msg = "Mail Sent Successfully."  
#     else:  
#         msg = "Mail Sending Failed."  
#     print(msg)


    

# from django.conf import settings                                                                                                                                                       
# from django.http import HttpResponse
# from twilio.rest import Client


# def broadcast_sms(request):
#     message_to_broadcast = ("Merci de faire partir de notre communauté")
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
#         if recipient:
#             client.messages.create(to=recipient,
#                                    from_=settings.TWILIO_NUMBER,
#                                    body=message_to_broadcast)
#     return HttpResponse("messages sent!", 200)

class CreateDonateur(APIView):
    def post(self,request):
        data=self.request.data
        serializer = DonateurMSerializer(data=data)
        error_message=None
        message='Votre inscription a bien été pris en charge merci de faire partir de notre communauté'
        if serializer.is_valid():
            error_message=self.validateDonateur(data)
            if not error_message:
                serializer.save()
                return Response({'message':message,'data':serializer.data,'status':200})
            return Response({'message':error_message,'status':400})
        return Response({'message':serializer.errors ,'status':400})

    def validateDonateur(self,donateur):
        error_message = None
        if (not donateur['last_name']):
            error_message="Svp entrer votre prenom"
        elif (not donateur['numero']):
            error_message="Svp entrer votre numero de téléphone"
        elif (not donateur['email']):
            error_message="Svp entrer votre email"
        elif (not donateur['user_name'] ):
            error_message="Svp entrer un username de 20 caractere min"
        return error_message

class CreateDonateurOr(APIView):
    def post(self,request):
        data=request.data
        serializer = DonateurOrSerializer(data=data)
        error_message=None
        message='Votre inscription a bien été pris en charge merci de faire partir de notre communauté '
        if serializer.is_valid():
            error_message=self.validateDonateur(data)
            if not error_message:
                serializer.save()
                return Response({'message':message,'data':serializer.data,'status':status.HTTP_200_OK})
            return Response({'message':error_message,'status':status.HTTP_400_BAD_REQUEST})
        return Response({'message':serializer.errors ,'status':status.HTTP_400_BAD_REQUEST})

    def validateDonateur(self,donateur):
        error_message = None
        if (not donateur['last_name']):
            error_message="Svp entrer votre prenom"
        elif (not donateur['numero']):
            error_message="Svp entrer votre numero de téléphone"
        elif (not donateur['email']):
            error_message="Svp entrer votre email"
        elif (not donateur['user_name']):
            error_message="Svp entrer un username de 5 caractere min"
        elif (not donateur['organisations']):
            error_message="Svp entrer le nom de votre organisations"
        return error_message

class CruddonateurOr(generics.RetrieveUpdateDestroyAPIView):
    model=DonateurUser
    permission_classes=[AllowAny]
    serializer_class=DonateurOrSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return DonateurUser.objects.filter(user_name=self.request.user.user_name)

class CruddonateurM(generics.RetrieveUpdateDestroyAPIView):
    model=DonateurUser
    permission_classes=[AllowAny]
    serializer_class=DonateurMSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return DonateurUser.objects.filter(user_name=self.request.user.user_name)


class EffectuerDonsArg(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            dons=EffectuerDonArge.objects.filter(donateur=self.request.user.user_name)
            serializer=EffectuerArgSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})

    def post(self,request):
        message='Merci pour votre contribution:\n nous vous contacterons dans peut'
        data=request.data
        if self.request.user.is_authenticated:
            data['donateur']=self.request.user.user_name
            serializer = EffectuerArgSerializer(data=data)
        else:
            data['donateur']='issa'
            serializer = EffectuerArgSerializer(data=data)
        error_message=None
        if serializer.is_valid():
            error_message=self.donEffectuer(data)
            if not error_message:
                serializer.save()
                return Response({'message':message,'data':serializer.data,'status':200})
            return Response({'message':error_message,'status':status.HTTP_400_BAD_REQUEST})
        return Response({'message':serializer.errors ,'status':status.HTTP_400_BAD_REQUEST})

    def donEffectuer(self,donateur):
        error_message = None
        if (not donateur['typeDons']):
            error_message="Svp choisissez le type de don"
        elif (not donateur['categorieV']):
            error_message="Svp entrer la categorie de votre don"
        elif (not donateur['cibleV']):
            error_message="Svp entrer votre email"
        elif (not donateur['montant'] ):
            error_message="Svp entrer un username de 5 caractere min"
        elif (not donateur['provider'] ):
            error_message="Svp entrer un username de 5 caractere min"
        return error_message

class EffectuerDonsObj(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            dons=EffectuerDonNature.objects.filter(donateur=self.request.user.user_name)
            serializer=EffectuerNatSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})

    def post(self,request):
        message='Merci pour votre contribution:\n nous vous contacterons dans peut'
        data=request.data
        if self.request.user.is_authenticated:
            data['donateur']=self.request.user.user_name
            serializer = EffectuerNatSerializer(data=data)
        else:
            data['donateur']='issa'
            serializer = EffectuerNatSerializer(data=data)
        error_message=None
        message='Merci pour votre contribution:\n nous vous contacterons dans peu'
        if serializer.is_valid():
            error_message=self.donEffectuer(data)
            if not error_message:
                serializer.save()
                return Response({'message':message,'data':serializer.data,'status':status.HTTP_200_OK})
            return Response({'message':error_message,'status':status.HTTP_400_BAD_REQUEST})
        return Response({'message':serializer.errors ,'status':status.HTTP_400_BAD_REQUEST})

    def donEffectuer(self,donateur):
        error_message = None
        if (not donateur['typeDons']):
            error_message="Svp entrer votre nom"
        elif (not donateur['categorieV']):
            error_message="Svp entrer votre prenom"
        elif (not donateur['cibleV']):
            error_message="Svp entrer votre numero de téléphone"
        elif (not donateur['categorieObjet']):
            error_message="Svp entrer votre email"
        elif (not donateur['typeObjet']):
            error_message="Svp entrer un username de 5 caractere min"
        elif (not donateur['lieu_reception']):
            error_message="Svp entrer un username de 5 caractere min"
        elif (not donateur['Etat']):
            error_message="Svp entrer un username de 5 caractere min"
        return error_message


#Liste des dons détailler ou non par utilisateur
class Argend(generics.RetrieveUpdateDestroyAPIView):
    model=EffectuerDonArge
    permission_classes=[AllowAny]
    serializer_class=EffectuerArgSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["donateur","typeDons","categorieV","cibleV","provider"]
    filterset_fields=["donateur","typeDons","categorieV","cibleV","provider"]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return EffectuerDonArge.objects.filter(donateur=self.request.user.user_name)

class Natured(generics.RetrieveUpdateDestroyAPIView):
    model=EffectuerDonNature
    permission_classes=[AllowAny]
    serializer_class=EffectuerNatSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["donateur","typeDons","categorieV","cibleV","categorieObjet","typeObjet"]
    filterset_fields=["donateur","typeDons","categorieV","cibleV","categorieObjet","typeObjet"]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return EffectuerDonNature.objects.filter(donateur=self.request.user.user_name)

class Argen(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            print(self.request.user)
            dons=EffectuerDonArge.objects.filter(donateur=self.request.user.user_name)
            serializer=EffectuerArgSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})

class Nature(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            dons=EffectuerDonNature.objects.filter(donateur=self.request.user.user_name)
            serializer=EffectuerNatSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})


class CibleArgent(APIView):
    def get(self,request,slug):
        dons=EffectuerDonArge.objects.filter(cibleV=slug,affecter=False)
        serializer=EffectuerArgSerializer(dons, many=True)
        return Response({'data':serializer.data,'status':status.HTTP_200_OK})
            
class CibleNature(APIView):
    def get(self,request,slug):
        dons=EffectuerDonNature.objects.filter(cibleV=slug,affecter=False)
        serializer=EffectuerNatSerializer(dons, many=True)
        return Response({'data':serializer.data,'status':status.HTTP_200_OK})
                    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DetailConecter(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        if self.request.user.is_authenticated:
            dons=DonateurUser.objects.filter(user_name=self.request.user.user_name)
            serializer=DonateurOrSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})


class EtatArge(APIView):
    def post(self,request):
        data=self.request.data
        print(data)
        don=EffectuerDonArge.objects.get(id=int(data["id"]))
        don.affecter=True
        don.distribuer=True
        don.updated_at=timezone.now()
        don.save(update_fields=['affecter','distribuer','updated_at'])
        return Response({'status':status.HTTP_200_OK})

class EtatNature(APIView):
    def post(self,request):
        data=self.request.data
        don=EffectuerDonNature.objects.get(id=int(data["id"]))
        don.affecter=True
        don.distribuer=True
        don.updated_at=timezone.now()
        don.save(update_fields=['affecter','distribuer','updated_at'])
        return Response({'status':status.HTTP_200_OK})

        


