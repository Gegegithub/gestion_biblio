from django.apps import AppConfig

class CustomAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_auth'  # Remplace 'auth' par 'custom_auth'
    label = 'custom_auth'  # Ce label est ok, il évite tout conflit avec l'application de base de Django
