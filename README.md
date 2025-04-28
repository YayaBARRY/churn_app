# 1. Application de Prédiction du Churn – Expresso Sénégal
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
