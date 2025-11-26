import json

# Chargement des données
def charger_donnees_etudiants(nom_fichier):
    try:
        with open(nom_fichier, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Sauvegarde des données
def sauvegarder_etudiants(etudiants, nom_fichier):
    with open(nom_fichier, 'w') as f:
        json.dump(etudiants, f, indent=4)

# Ajouter un étudiant
def ajouter_etudiant():
    nom = input("Entrez le nom de l'étudiant : ")
    etudiant = {"nom": nom, "matières": {}}
    return etudiant

# Ajouter une note
def ajouter_note(etudiant):
    matiere = input("Entrez le nom de la matière : ")
    note = float(input(f"Entrez la note pour {matiere}: "))
    etudiant["matières"][matiere] = note

# Afficher les étudiants avec leur moyenne
def afficher_etudiants(etudiants):
    for e in etudiants:
        print(f"\nNom : {e['nom']}")
        for matiere, note in e["matières"].items():
            print(f"{matiere}: {note}")
        moyenne = calcul_moyenne(e)
        print(f"Moyenne générale: {moyenne:.2f}")

# Modifier un étudiant
def modifier_etudiant(etudiants):
    nom = input("Entrez le nom de l'étudiant à modifier : ")
    for e in etudiants:
        if e["nom"] == nom:
            ajouter_note(e)
            print("Modification effectuée.")
            return
    print("Étudiant non trouvé.")

# Supprimer un étudiant
def supprimer_etudiant(etudiants):
    nom = input("Entrez le nom de l'étudiant à supprimer : ")
    for i, e in enumerate(etudiants):
        if e["nom"] == nom:
            del etudiants[i]
            print("Étudiant supprimé.")
            return
    print("Étudiant non trouvé.")

# Calculer la moyenne d'un étudiant
def calcul_moyenne(etudiant):
    if etudiant["matières"]:
        return sum(etudiant["matières"].values()) / len(etudiant["matières"])
    return 0.0

# Programme principal
etudiants = charger_donnees_etudiants("etudiants.json")

while True:
    print("\nMenu :")
    print("1. Ajouter un étudiant")
    print("2. Ajouter une note")
    print("3. Modifier un étudiant")
    print("4. Supprimer un étudiant")
    print("5. Afficher les étudiants avec moyenne")
    print("6. Sauvegarder et quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        etudiant = ajouter_etudiant()
        etudiants.append(etudiant)
    elif choix == "2":
        nom = input("Entrez le nom de l'étudiant : ")
        for e in etudiants:
            if e["nom"] == nom:
                ajouter_note(e)
                break
    elif choix == "3":
        modifier_etudiant(etudiants)
    elif choix == "4":
        supprimer_etudiant(etudiants)
    elif choix == "5":
        afficher_etudiants(etudiants)
    elif choix == "6":
        sauvegarder_etudiants(etudiants, "etudiants.json")
        print("Données sauvegardées. Fin du programme.")
        break
    else:
        print("Option incorrecte, veuillez réessayer.")
