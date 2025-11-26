
etudiants = []
etudiant = {
    "nom": "Jean Dupont",
    "matières": {"Math": 15.5, "Physique": 14.0}
}
etudiants.append(etudiant)

# Affichage des étudiants
for e in etudiants:
    print(f"Nom : {e['nom']}")
    for matiere, note in e["matières"].items():
        print(f"{matiere}: {note}")
