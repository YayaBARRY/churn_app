# 1. Application de Prédiction du Churn des Clients d'Expresso Sénégal
Cette application Flask prédit le risque de désabonnement des clients de l'opérateur Expresso Sénégal à partir de données client. Elle est déployée gratuitement sur Render.


# 2. Fonctionnalités
- Formulaire utilisateur avec saisie des données client 
- Prédiction avec un modèle Machine Learning (`KNN`) 
- Affichage du résultat de la prédiction avec probabilité
- Authentification simple par identifiants 


# 3. Technologies utilisées
- Python / Flask
- Scikit-learn, Joblib, Pandas
- Bootstrap 5 (pour le front-end)
- Déploiement via GitHub + Docker + Render


# 4. Installation locale

# 4.1. Cloner le dépôt
```bash
git clone https://github.com/ton-utilisateur/nom-du-repo.git
cd nom-du-repo
```

# 4.2. Créer un environnement virtuel et installer les dépendances
```bash
python -m venv venv
venv\Scripts\activate  # (Windows)

pip install -r requirements.txt
```

# 4.3. Lancer l'application localement
```bash
python app.py
```

# 5. Déploiement sur Render

# 6. Déclencher un déploiement automatique via GitHub
Chaque `git push` déclenchera un nouveau déploiement.

# 7. Structure des pages
- `/login` – page de connexion
- `/` – formulaire principal + prédiction

## Développé par
**Mamadou Yaya BARRY – 2025**  
Étudiant en Master 2 MIAGE à l'UGB, passionné de Data & IA.


![Capture d'écran 2025-04-27 031533](https://github.com/user-attachments/assets/7847ec41-e046-473f-8c64-571404e8488c)
![Capture d'écran 2025-04-27 041812](https://github.com/user-attachments/assets/cc5ec773-c3ec-4d3a-a9ab-a4325881d96b)
![Capture d'écran 2025-04-27 041923](https://github.com/user-attachments/assets/f87bb9f4-5e1f-475a-ac99-98f12568f53f)
![Capture d'écran 2025-04-27 041942](https://github.com/user-attachments/assets/474e2963-3d2d-4a08-9e4b-5c5ed4f3acbf)
![Capture d'écran 2025-04-27 042122](https://github.com/user-attachments/assets/4a993f8c-512f-48cb-9869-3649c4b8568e)
