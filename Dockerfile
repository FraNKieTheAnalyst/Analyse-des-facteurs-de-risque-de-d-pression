# Utiliser une image de base Python
FROM python:3.11-slim

# Installer les dépendances nécessaires pour Rust (comme curl)
RUN apt-get update && apt-get install -y curl build-essential

# Installer Rust et Cargo via rustup
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Permettre l'affichage immédiat des instructions et messages de log dans les journaux de Knative
# Ajouter Cargo au PATH
ENV PATH="/root/.cargo/bin:${PATH}"
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
ENV PORT=8080

# Définir le répertoire de travail dans le conteneur
WORKDIR $APP_HOME

# Copier les fichiers du projet dans le conteneur
COPY . ./
COPY Super_Vector_Machine.pkl /app/

# Exposer le port utilisé par l'application (8080 pour Cloud Run)
EXPOSE 8080
# Installer les dépendances de production.
# Exécute pip install pour les packages spécifiés dans requirements.txt
RUN pip install --upgrade pip
RUN cargo --version
RUN rustc --version

RUN pip install -r requirements.txt

# Exécuter le service web au démarrage du conteneur. Ici, nous utilisons le serveur web gunicorn,
# avec un processus worker et 8 threads.
# Pour des environnements avec plusieurs cœurs de CPU, augmentez le nombre de workers
# pour qu'il soit égal au nombre de cœurs disponibles.
# Le timeout est réglé sur 0 pour désactiver les timeouts des workers pour permettre à Cloud Run de gérer l'échelonnement des instances.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
#CMD exec uvicorn main:app --host 0.0.0.0 --port $PORT

#la ligne ci dessous permet de contenariser l'application et publier l'image docker sur le cloud
#activer artefact registry et cloud run
#gcloud builds submit --tag gcr.io/projetprediredepression/deploiement
#gcloud run deploy --image gcr.io/projetprediredepression/deploiement --platform managed 