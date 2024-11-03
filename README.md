# LinkLite 🔗

LinkLite est un raccourcisseur d'URL moderne et élégant construit avec Django et TailwindCSS. Cette application permet de transformer facilement de longs liens en URLs courtes et traçables.

https://github.com/user-attachments/assets/d969d353-5372-4d11-94da-64e0bad19f96

## ✨ Fonctionnalités

- 🔄 Raccourcissement d'URL instantané
- 📊 Statistiques de clics en temps réel
- 📱 Interface responsive et moderne
- 🎯 Suivi du nombre total de liens créés
- 📈 Analyse du trafic global

## 🚀 Technologies Utilisées

- **Backend**: Django 3.1
- **Frontend**: TailwindCSS 3.8.0
- **Package**: django-tailwind

## 🛠 Installation

1. Clonez le repository
```bash
git clone https://github.com/votre-username/LinkLite.git
cd LinkLite
```

2. Créez un environnement virtuel
```bash
python -m venv env
source env/bin/activate  # Sur Windows: env\Scripts\activate
```

3. Installez les dépendances
```bash
pip install -r requirements.txt
```

4.Configurez la base de données
```bash
python manage.py runserver
```

5. Installez et compilez les assets TailwindCSS
```bash
python manage.py tailwind install
python manage.py tailwind build
```

6. Lancez le serveur
```bash
python manage.py runserver
```

🌐 Utilisation

Accédez à http://localhost:8000
Collez votre URL longue dans le champ
Cliquez sur "Raccourcir"
Copiez et partagez votre lien court !

📊 Statistiques Disponibles

Nombre total de liens créés
Nombre total de clics
Taux de disponibilité du service

## 🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à :

Fork le projet
Créer votre branche (git checkout -b feature/AmazingFeature)
Commit vos changements (git commit -m 'Add some AmazingFeature')
Push sur la branche (git push origin feature/AmazingFeature)
Ouvrir une Pull Request

📝 Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

👏 Remerciements

Django pour le framework backend
TailwindCSS pour le framework CSS
django-tailwind pour l'intégration


Fait avec ❤️ et ☕️

