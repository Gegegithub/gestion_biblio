# Bibliothèque Numérique

Une application web moderne de gestion de bibliothèque développée avec Django, proposant une interface utilisateur élégante et intuitive.

## 📚 Présentation

Ce projet est une application de gestion de bibliothèque qui permet aux utilisateurs de parcourir un catalogue de livres, de consulter leurs informations personnelles et de gérer leurs emprunts. L'interface a été soigneusement conçue avec un thème de couleurs moderne aux teintes bleu foncé et accents vert/jaune.

## ✨ Fonctionnalités

- **Catalogue de livres** : Parcourez la collection complète de livres disponibles
- **Recherche intuitive** : Trouvez rapidement des livres grâce à la barre de recherche
- **Profil utilisateur** : Consultez et gérez vos informations personnelles
- **Gestion des emprunts** : Suivez l'historique de vos emprunts
- **Interface responsive** : Expérience utilisateur optimisée sur tous les appareils
- **Navigation simplifiée** : Menu latéral déroulant pour une expérience utilisateur fluide

## 🎨 Design

L'application utilise une palette de couleurs soigneusement sélectionnée :
- Fond principal : Bleu très foncé (#040f3a)
- Conteneurs : Bleu foncé (#0D255A)
- Boutons et accents : Vert (#5EB727)
- Effets au survol : Jaune (#e4e435)
- Texte : Blanc pour un contraste maximal

Les informations sont présentées de façon claire et organisée, avec des sections déroulantes pour une meilleure lisibilité et une navigation fluide.

## 🔧 Technologies utilisées

- **Backend** : Django (Python)
- **Frontend** : HTML, CSS, JavaScript
- **Base de données** : SQLite (développement)
- **Bibliothèques** : Bootstrap, Font Awesome

## 📋 Prérequis

- Python 3.8 ou supérieur
- Django 3.2 ou supérieur

## 🚀 Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/votre-username/biblio.git
cd biblio
```

2. Créez et activez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Appliquez les migrations :
```bash
python manage.py migrate
```

5. Créez un super utilisateur (facultatif) :
```bash
python manage.py createsuperuser
```

6. Lancez le serveur de développement :
```bash
python manage.py runserver
```

7. Accédez à l'application dans votre navigateur : http://127.0.0.1:8000/

## 📱 Captures d'écran

![Page d'accueil](captures/accueil.png)
![Profil utilisateur](captures/profil.png)
*(Note: Remplacez avec vos propres captures d'écran)*

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Auteur

- **Votre Nom** - [votre-username](https://github.com/votre-username)

---

Développé avec ❤️ et ☕ 