from django.urls import path,include
from .categorie import*
from .cible import*
from .affecterdons import*
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns=format_suffix_patterns([
    path('objetca/', ListCategorieO.as_view(),name='list-objet'),
    path('objetcad/<int:pk>/', CategorieO.as_view(),name='detail-objet'),
    path('vulnerableca/', ListCategorieVulnerable.as_view(),name='list-vulnerable'),
    path('vulnerablecad/<int:pk>/', CategorieVulnerable.as_view(),name='detail-vulnerable'),
    #
    path('objetty/', ListTypeOjet.as_view(),name='list-tobjet'),
    path('objettyd/<int:pk>/', TypeOjet.as_view(),name='detail-tobjet'),
    path('vulnerablety/', ListTypeVulnerable.as_view(),name='list-tvulnerable'),
    path('vulnerabletyd/<int:pk>/', TypeVulnerable.as_view(),name='detail-tvulnerable'),

    #Lister tout les donateur pour l'admin
    path('listdonateur/',ListDonateur.as_view(),name='registers-donArg'),
    path('listdonateurd/<int:pk>/',ListDonateurd.as_view(),name='registers-donOjets'),

    #Lister tout les dons pour l'admin
    path('listargea/', ListDonArgea.as_view(),name='list-donara'),
    path('affecterargent/<int:pk>/', ListDonArgeda.as_view(),name='detail-donarad'),
    path('listnaturea/', ListDonNaturea.as_view(),name='list-donna'),
    path('affecterobjet/<int:pk>/', ListDonNaturedad.as_view(),name='detail-donnad')
])