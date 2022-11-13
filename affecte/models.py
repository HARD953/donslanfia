from django.db import models

# Create your models here.

class Vulnerable_categorie(models.Model):
    #Objet
    categorie_vulnerable=models.CharField(max_length=100,primary_key=True)
    create=models.DateTimeField(auto_now_add=True)
    # x=["Etat","photo","lieu_reception","donateur","typeD","categorieV","cibleV","montant","provider","categorieObjet","typeObjet"]
    def __str__(self):
        return "{}".format(self.categorie_vulnerable)
class Vulnerable_cible(models.Model):
    #Objet
    categorie_vulnerable=models.ForeignKey(Vulnerable_categorie,on_delete=models.CASCADE,default=1)
    cible_vulnerable=models.CharField(max_length=100,default='null')
    create=models.DateTimeField(auto_now_add=True)
    # x=["Etat","photo","lieu_reception","donateur","typeD","categorieV","cibleV","montant","provider","categorieObjet","typeObjet"]
    def __str__(self):
        return "{}".format(self.cible_vulnerable)

    # @staticmethod
    # def get_vulnerable_by_id(ids):
    #     return Vulnerable_cible.objects.filter (id__in=ids)
    # @staticmethod
    # def get_all_vulnerable():
    #     return Vulnerable_cible.objects.all()

    # @staticmethod
    # def get_all_vulnerable_by_categoryid(category_id):
    #     if category_id:
    #         return Vulnerable_cible.objects.filter (category=category_id)
    #     else:
    #         return Vulnerable_cible.get_all_vulnerable()

class Categorie_obj(models.Model):
    #Objet
    categorie_objet=models.CharField(max_length=100,primary_key=True)
    # x=["Etat","photo","lieu_reception","donateur","typeD","categorieV","cibleV","montant","provider","categorieObjet","typeObjet"]
    def __str__(self):
        return "{}".format(self.categorie_objet)

class Type_obj(models.Model):
    categorie_objet=models.ForeignKey(Categorie_obj,on_delete=models.CASCADE,default=1)
    type_objet=models.CharField(max_length=100,default='null')
    create=models.DateTimeField(auto_now_add=True)
    # x=["Etat","photo","lieu_reception","donateur","typeD","categorieV","cibleV","montant","provider","categorieObjet","typeObjet"]
    def __str__(self):
        return "{}".format(self.type_objet)