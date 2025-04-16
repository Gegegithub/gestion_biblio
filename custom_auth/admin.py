from django.contrib import admin
from .models import CustomUser

# Enregistre le modèle CustomUser dans l'admin
admin.site.register(CustomUser)

