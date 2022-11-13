from rest_framework import serializers
from .models import *
from utilisateur.models import*
from django.contrib.auth.models import User

class CateObjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie_obj
        fields = "__all__"

class TypeObjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_obj
        fields = "__all__"

class VulnerableCateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerable_categorie
        fields = "__all__"

class VulnerableCibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerable_cible
        fields = "__all__"


class EffectuerArgSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectuerDonArge
        fields = ["id","donateur","typeDons","categorieV","cibleV","montant","provider","affecter"]

class EffectuerNatSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectuerDonNature
        fields = ["id","donateur","typeDons","categorieV","cibleV","categorieObjet","typeObjet","lieu_reception","Etat","photo","affecter"]