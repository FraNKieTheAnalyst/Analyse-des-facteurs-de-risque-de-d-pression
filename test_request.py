import requests

# URL de base de l'API
url_base = 'http://127.0.0.1:8000'

# Test du endpoint d'accueil
response = requests.get(f"{url_base}/")
print("Réponse du endpoint d'accueil:", response.text)
# Données d'exemple pour la prédiction
donnees_predire = {
    "Age": 20,
    "Work_Pressure": 4,
    "Job_Satisfaction": 5,
    "Have_you_ever_had_suicidal_thoughts": 1,
    "Work_Hours":  11,
    "Financial_Stress": 5,
    "Family_History_of_Mental_Illness": 1,
    "Profession_Education_Enseignement": 1,
    "Profession_entrepreneur_consultant": 0,
    "Profession_Sciences_Recherche": 0,
    "Dietary_Habits_Unhealthy": 1,
    "Sleep_Duration_Less_than_5_hours": 0
}

# Test du endpoint de prédiction
response = requests.post(f"{url_base}/predire", json=donnees_predire)  # Removed the trailing slash
print("Réponse du endpoint de prédiction:", response.text)


# Données d'exemple pour la prédiction avec haute probabilité de diabète
donnees_predire_haute_proba_diabete = {
    "Age": 30,
    "Work_Pressure": 4,
    "Job_Satisfaction": 5,
    "Have_you_ever_had_suicidal_thoughts": 0,
    "Work_Hours":  5,
    "Financial_Stress": 2,
    "Family_History_of_Mental_Illness": 0,
    "Profession_Education_Enseignement": 0,
    "Profession_entrepreneur_consultant": 1,
    "Profession_Sciences_Recherche": 0,
    "Dietary_Habits_Unhealthy": 0,
    "Sleep_Duration_Less_than_5_hours": 0
}

# Test du endpoint de prédiction
response = requests.post(f"{url_base}/predire", json=donnees_predire_haute_proba_diabete)
print("Réponse du endpoint de prédiction:", response.text)