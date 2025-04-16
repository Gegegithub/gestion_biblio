from django.urls import path
from . import views

app_name = 'bibliotheque'

urlpatterns = [
    path('', views.home, name='home'),
    path('livre/<int:book_id>/', views.detail, name='detail'),
    path('mes-emprunts/', views.mes_emprunts, name='mes_emprunts'),
    path('emprunter/<int:book_id>/', views.emprunter_livre, name='emprunter_livre'),
    path('retourner/<int:livre_id>/', views.retourner_livre, name='retourner_livre'),
    path('profil/', views.profil, name='profil'),
] 