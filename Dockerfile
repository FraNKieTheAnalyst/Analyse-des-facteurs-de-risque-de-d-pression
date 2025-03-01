# Utiliser une image de base Python
FROM python:3.13-slim


# Permettre l'affichage immédiat des instructions et messages de log dans les journaux de Knative
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app

# Définir le répertoire de travail dans le conteneur
WORKDIR $APP_HOME

# Copier les fichiers du projet dans le conteneur
COPY . ./

# Installer les dépendances de production.
# Exécute pip install pour les packages spécifiés dans requirements.txt
RUN pip install -r requirements.txt

# Exécuter le service web au démarrage du conteneur. Ici, nous utilisons le serveur web gunicorn,
# avec un processus worker et 8 threads.
# Pour des environnements avec plusieurs cœurs de CPU, augmentez le nombre de workers
# pour qu'il soit égal au nombre de cœurs disponibles.
# Le timeout est réglé sur 0 pour désactiver les timeouts des workers pour permettre à Cloud Run de gérer l'échelonnement des instances.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
#la ligne ci dessous permet de contenariser l'application et publier l'image docker sur le cloud
#activer artefact registry et cloud run
#gcloud builds submit --tag gcr.io/projetprediredepression/deploiement