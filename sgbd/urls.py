from django.contrib import admin
from django.urls import path, include
from custom_auth import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("custom_auth.urls", namespace="custom_auth")),  # Inclure les URLs de l'app "custom_auth"
    path("admin/", admin.site.urls),  # Interface d'administration Django
    path("__reload__/", include("django_browser_reload.urls")),  # Pour recharger le serveur en mode dev
    path("bibliotheque/", include("bibliotheque.urls")),  # Inclure les URLs de l'app "bibliotheque"
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
