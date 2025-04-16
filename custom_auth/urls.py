from django.urls import path
from . import views

app_name = 'custom_auth'

urlpatterns = [
    path('', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('profil/', views.profil, name='profil'),
]
