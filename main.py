from pydantic import BaseModel  # Utilisé pour la validation des données
import numpy as np
import pandas as pd  
import joblib  # Utilisé pour charger le modèle sauvegardé
from flask import Flask, request, jsonify  # Flask est un micro-framework pour les applications web
import os


# Charger le modèle SVM depuis le disque
modele = joblib.load('Super_Vector_Machine.pkl')
# Définition du schéma des données d'entrée avec Pydantic
# Cela garantit que les données reçues correspondent aux attentes du modèle
class DonneesEntree(BaseModel):
    Age: int
    Work_Pressure: float
    Job_Satisfaction:float
    Have_you_ever_had_suicidal_thoughts: int
    Work_Hours:  int
    Financial_Stress: int 
    Family_History_of_Mental_Illness: int
    City_Villes_de_lOuest: bool 
    Profession_Education_Enseignement: bool 
    Profession_Sciences_Recherche: bool
    Profession_entrepreneur_consultant: bool
    Dietary_Habits_Unhealthy: bool
    Sleep_Duration_Less_than_5_hours: bool
    


# Création de l'instance de l'application Flask
app = Flask(__name__)

# Définition de la route racine qui retourne un message de bienvenue
@app.route("/", methods=["GET"])
def accueil():
    """ Endpoint racine qui fournit un message de bienvenue. """
    return jsonify({"message": "Bienvenue sur l'API de prediction pour le diagnostic de la depression"})

# Définition de la route pour les prédictions de la dépression
@app.route("/predire", methods=["POST"])
def predire():
    """
    Endpoint pour les prédictions en utilisant le modèle chargé.
    Les données d'entrée sont validées et transformées en DataFrame pour le traitement par le modèle.
    """
    if not request.json:
        return jsonify({"erreur": "Aucun JSON fourni"}), 400
    
    
    try:
        # Extraction et validation des données d'entrée en utilisant Pydantic
        donnees = DonneesEntree(**request.json)
        donnees_df = pd.DataFrame([donnees.dict()])  # Conversion en DataFrame

        # Utilisation du modèle pour prédire et obtenir les probabilités
        predictions = modele.predict(donnees_df)
        probabilities = modele.predict_proba(donnees_df)[:, 1]  # Probabilité de la classe positive (depression)

        # Compilation des résultats dans un dictionnaire
        resultats = donnees.dict()
        resultats['prediction'] = int(predictions[0])
        resultats['probabilite_depression'] = probabilities[0]

        # Renvoie les résultats sous forme de JSON
        return jsonify({"resultats": resultats})
    except Exception as e:
        # Gestion des erreurs et renvoi d'une réponse d'erreur
        return jsonify({"erreur": str(e)}), 400

# Point d'entrée pour exécuter l'application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Utilisation du port Cloud Run (par défaut 8080)
    app.run(debug=True, host="0.0.0.0", port=port) 


