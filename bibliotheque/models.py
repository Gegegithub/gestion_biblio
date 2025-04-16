from django.db import models
from custom_auth.models import CustomUser

class Book(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=150)
    date_publication = models.DateField()
    genre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(max_length=255, upload_to="image/", blank=True, null=True)  
    disponible = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.titre

class Emprunt(models.Model):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    utilisateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    livre = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour = models.DateTimeField(null=True, blank=True)
    age_emprunt = models.PositiveIntegerField(null=True, blank=True)
    sexe_emprunt = models.CharField(max_length=1, choices=SEXE_CHOICES, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.age_emprunt = self.utilisateur.age
        self.sexe_emprunt = self.utilisateur.sexe
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.livre.titre}" 