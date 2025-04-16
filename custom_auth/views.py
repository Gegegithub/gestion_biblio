from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from custom_auth.models import CustomUser

def inscription(request):
    if request.method == "POST":
        # Récupération des données du formulaire
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        age = request.POST.get("age")
        sexe = request.POST.get("sexe")

        # Vérification des mots de passe
        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, "inscription.html")

        # Vérification de l'unicité du nom d'utilisateur et de l'email
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà pris.")
            return render(request, "inscription.html")
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return render(request, "inscription.html")

        # Création de l'utilisateur
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            age=age,
            sexe=sexe
        )

        # Connexion automatique après l'inscription
        login(request, user)
        messages.success(request, "Inscription réussie !")
        return redirect("bibliotheque:home")

    return render(request, "inscription.html")

def connexion(request):
    error_message = ""

    if request.method == "POST":
        username_or_email = request.POST.get("username_or_email")
        password = request.POST.get("password")

        # Vérifier si l'utilisateur a entré un email au lieu d'un username
        user = CustomUser.objects.filter(email=username_or_email).first()
        if user:
            username_or_email = user.username

        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            return redirect("bibliotheque:home")
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."

    return render(request, "connexion.html", {"error": error_message})

@login_required
def profil(request):
    return render(request, "profil.html", {"utilisateur": request.user})
