import requests

# URL de base de l'API
url_base = 'http://127.0.0.1:8080' #a été utilisé pour tester l'API en local
#url_base = 'https://deploiement-744655853198.europe-west9.run.app' 
# Test du endpoint d'accueil
response = requests.get(f"{url_base}/")
print("Réponse du endpoint d'accueil:", response.text)
# Données d'exemple pour la prédiction
donnees_predire = {
    "Age": 37,
    "Work_Pressure": 2,
    "Job_Satisfaction": 4,
    "Have_you_ever_had_suicidal_thoughts": 0,
    "Work_Hours":  12,
    "Financial_Stress": 5,
    "Family_History_of_Mental_Illness": 1,
    "City_Villes_de_lOuest": 1,
    "Profession_Education_Enseignement": 1,
    "Profession_Sciences_Recherche": 0,
    "Profession_entrepreneur_consultant": 0,
    "Dietary_Habits_Unhealthy": 1,
    "Sleep_Duration_Less_than_5_hours": 1
        
}


# Test du endpoint de prédiction
response = requests.post(f"{url_base}/predire", json=donnees_predire)  # Removed the trailing slash
print("Réponse du endpoint de prédiction:", response.text)


# Données d'exemple pour la prédiction avec haute probabilité de diabète
donnees_predire_haute_proba_depression = {
    "Age": 22,
    "Work_Pressure": 60,                            
    "Job_Satisfaction": 0,
    "Have_you_ever_had_suicidal_thoughts": 1,
    "Work_Hours": 40,
    "Financial_Stress": 10,
    "Family_History_of_Mental_Illness": 1,
    "City_Villes_de_lOuest": 1,
    "Profession_Education_Enseignement": 1,
    "Profession_Sciences_Recherche": 0,
    "Profession_entrepreneur_consultant": 0,
    "Dietary_Habits_Unhealthy": 1,
    "Sleep_Duration_Less_than_5_hours": 1 
}

# Test du endpoint de prédiction
response = requests.post(f"{url_base}/predire", json=donnees_predire_haute_proba_depression)
print("Réponse du endpoint de prédiction:", response.text)