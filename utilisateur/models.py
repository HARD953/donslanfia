from ast import operator
from distutils.command.upload import upload
from locale import currency
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin, AbstractBaseUser,BaseUserManager
from affecte.models import*
from django.utils import timezone
from django.conf import settings

# Create your models here.
class CustumerAccountManager(BaseUserManager):
    def create_user(self, email, user_name,first_name,password, **other_fields):
        if not email:
            raise ValueError("you must provide a email address")
        email=self.normalize_email(email)
        user=self.model(email=email,user_name=user_name,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name,first_name, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be assigned to is_superuser=True.')     
        return self.create_user(email, user_name,first_name,**other_fields)

class DonateurUser(AbstractBaseUser,PermissionsMixin):
    user_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30,default="ras")
    email=models.EmailField(max_length=255,unique=True)
    numero=models.CharField(max_length=30)
    organisations=models.CharField(max_length=30,default="null")
    email1=models.EmailField(max_length=255)
    adresse=models.CharField(max_length=30,default="null")
    numero1=models.CharField(max_length=30)
    last_login = models.DateTimeField(('last_login'), default=timezone.now())
    objects=CustumerAccountManager()
    # adresse=models.CharField(max_length=300, blank=True, null=True)
    # about_me=models.TextField(max_length=500, blank=True, null=True)
    # create=models.DateTimeField(auto_now_add=True)
    # profile_image=models.ImageField(null=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    # is_user=models.BooleanField(default=False)
    # is_agent=models.BooleanField(default=False)

    x={
    "first_name":"kouassi",
    "last_name":"herver",
    "email":"her@gmail.com",
    "numero":"08596129",
    "organisations":"Ministere de la famine et de l'enfance",
    "password":"herve01"
    }
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_name','first_name']
    
    def __str__(self):
        return self.email

class EffectuerDonArge(models.Model):
    #Espece
    donateur=models.CharField(max_length=30,default='issa')
    typeDons=models.CharField(max_length=30,default='null')
    categorieV=models.CharField(max_length=30,default='null')
    cibleV=models.CharField(max_length=100,default='null')
    create=models.DateTimeField(auto_now_add=True)
    montant=models.CharField(max_length=100,default='null')
    provider=models.CharField(max_length=100,default='null')
    typePersonne=models.CharField(max_length=100,default='null')
    provenanced=models.CharField(max_length=100,default='null')
    affecter = models.BooleanField (default=False)
    distribuer = models.BooleanField (default=False)
    description=models.CharField(max_length=100,default='null')
    amount=models.CharField(max_length=100,default='null')
    currency=models.CharField(max_length=100,default='null')
    matadata=models.CharField(max_length=100,default='null')
    operator_id=models.CharField(max_length=100,default='null')
    payement_date=models.CharField(max_length=100,default='null')
    payement_method=models.CharField(max_length=100,default='null')
    status=models.CharField(max_length=100,default='null')


    # x=["Etat","photo","lieu_reception","donateur","typeD","categorieV","cibleV","montant","provider","categorieObjet","typeObjet"]
    def __str__(self):
        return "{}".format(self.donateur)
class EffectuerDonNature(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.donateur), filename])
    #Objet
    donateur=models.CharField(max_length=30,default='issa')
    typeDons=models.CharField(max_length=30,default='null')
    categorieV=models.CharField(max_length=30,default='null')
    cibleV=models.CharField(max_length=100,default='null')
    categorieObjet=models.CharField(max_length=100,default='null')
    typeObjet=models.CharField(max_length=30,default='null')
    lieu_reception=models.CharField(max_length=100,default='null')
    photo=models.ImageField(upload_to=nameFile,blank=True)
    Etat=models.CharField(max_length=100,default='null')
    typePersonne=models.CharField(max_length=100,default='null')
    provenanced=models.CharField(max_length=100,default='null')
    titre=models.CharField(max_length=100,default='null')
    description=models.TextField(max_length=100,default='null')
    affecter = models.BooleanField (default=False)
    distribuer = models.BooleanField (default=False)
    create=models.DateTimeField(auto_now_add=True)

    # x=["Etat","photo","lieu_reception","donateur","typeD","categorieV","cibleV","montant","provider","categorieObjet","typeObjet"]
    def __str__(self):
        return "{}".format(self.donateur)


   



