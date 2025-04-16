from django.contrib import admin
from .models import Book, Emprunt

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'genre', 'disponible', 'date_publication')
    list_filter = ('genre', 'disponible')
    search_fields = ('titre', 'auteur', 'description')
    ordering = ('titre',)

@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'livre', 'date_emprunt', 'date_retour')
    list_filter = ('date_emprunt', 'date_retour')
    search_fields = ('utilisateur__username', 'livre__titre')
    ordering = ('-date_emprunt',) 