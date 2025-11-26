def ajouter_etudiant():
    nom = input("Entrez le nom de l'étudiant : ")
    etudiant = {"nom": nom, "matières": {}}
    return etudiant

def afficher_etudiants(etudiants):
    for e in etudiants:
        print(f"Nom : {e['nom']}")
        for matiere, note in e["matières"].items():
            print(f"{matiere}: {note}")

def calcul_moyenne(etudiant):
    if etudiant["matières"]:
        return sum(etudiant["matières"].values()) / len(etudiant["matières"])
    return 0.0
