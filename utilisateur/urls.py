from django.urls import path,include
from .views import*
from rest_framework.urlpatterns import format_suffix_patterns

from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns=format_suffix_patterns([
    #Crée des donateur
    path('donateurm/', CreateDonateur.as_view(),name='registers-donateurm'),
    path('donateurorg/',CreateDonateurOr.as_view(),name='registers-donateurorg'),

    path('cdonateurm/<int:pk>/', CruddonateurM.as_view()),
    path('cdonateurorg/<int:pk>/',CruddonateurOr.as_view()),
    #Effectuer des dons
    path('detailconnecte/', DetailConecter.as_view(),name='detail-connecte'),

    path('efdoargent/',EffectuerDonsArg.as_view(),name='registers-donArg'),
    path('efdoobjet/',EffectuerDonsObj.as_view(),name='registers-donOjets'),
    #Afficher ses dons
    path('argent/', Argen.as_view(),name='detail-donard'),
    path('natures/', Nature.as_view(),name='detail-donnd'),
    path('etatsargent/', EtatArge.as_view(),name='etatsa'),
    path('etatsnature/', EtatNature.as_view(),name='etatsn'),

    path('cibleargent/<str:slug>/', CibleArgent.as_view(),name='cible-donard'),
    path('ciblenatures/<str:slug>/', CibleNature.as_view(),name='cible-donnd'),

    path('argend/<int:pk>/', Argend.as_view(),name='detail-donard'),
    path('natured/<int:pk>/', Natured.as_view(),name='detail-donnd'),
    #connexion
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', BlacklistTokenUpdateView.as_view(), name='token_refresh'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
])