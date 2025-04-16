from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Emprunt

def home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        livres = Book.objects.filter(titre__icontains=search_query) | Book.objects.filter(auteur__icontains=search_query)
    else:
        livres = Book.objects.all()
    return render(request, "home.html", {"livres": livres, "search_query": search_query})

def detail(request, book_id):
    livre = get_object_or_404(Book, id=book_id)
    return render(request, "detail.html", {"livre": livre})

@login_required
def mes_emprunts(request):
    emprunts = Emprunt.objects.filter(utilisateur=request.user)
    return render(request, "mes_emprunts.html", {"emprunts": emprunts})

@login_required
def emprunter_livre(request, book_id):
    livre = get_object_or_404(Book, id=book_id)
    
    # Vérifier si l'utilisateur a déjà emprunté ce livre
    emprunt_existant = Emprunt.objects.filter(utilisateur=request.user, livre=livre).exists()
    
    if emprunt_existant:
        messages.error(request, f"Vous avez déjà emprunté '{livre.titre}'.")
        return redirect('bibliotheque:detail', book_id=book_id)
    
    if livre.disponible > 0:
        Emprunt.objects.create(utilisateur=request.user, livre=livre)
        livre.disponible -= 1
        livre.save()
        messages.success(request, f"Vous avez emprunté '{livre.titre}'.")
    else:
        messages.error(request, "Ce livre n'est plus disponible pour l'instant.")
    
    return redirect('bibliotheque:detail', book_id=book_id)

@login_required
def retourner_livre(request, livre_id):
    livre = get_object_or_404(Book, id=livre_id)
    emprunt = Emprunt.objects.filter(livre=livre, utilisateur=request.user).first()

    if emprunt:
        emprunt.delete()
        livre.disponible += 1
        livre.save()
        messages.success(request, "Le livre a été retourné avec succès.")

    return redirect('bibliotheque:mes_emprunts')

@login_required
def profil(request):
    # Récupérer l'historique des emprunts pour l'utilisateur
    historique_emprunts = Emprunt.objects.filter(utilisateur=request.user).order_by('-date_emprunt')[:5]
    
    return render(request, "profil.html", {
        "utilisateur": request.user,
        "historique_emprunts": historique_emprunts
    }) 