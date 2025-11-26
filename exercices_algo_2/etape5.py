import json

def sauvegarder_etudiants(etudiants, nom_fichier):
    with open(nom_fichier, 'w') as f:
        json.dump(etudiants, f)

def charger_donnees_etudiants(nom_fichier):
    try:
        with open(nom_fichier, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
