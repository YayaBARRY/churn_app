# Image officielle légère et plus récente
FROM python:3.13-slim

# Dossier de travail
WORKDIR /app

# Copier les fichiers de l'app
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port Flask
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]