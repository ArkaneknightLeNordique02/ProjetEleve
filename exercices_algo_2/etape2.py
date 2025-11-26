# Menu interactif
while True:
    print("\nMenu :")
    print("1. Ajouter un étudiant")
    print("2. Afficher les étudiants")
    print("3. Quitter")
    
    choix = input("Choisissez une option : ")

    if choix == "1":
        print("Ajout d'un étudiant.")
    elif choix == "2":
        print("Liste des étudiants.")
    elif choix == "3":
        print("Fin du programme.")
        break
    else:
        print("Option incorrecte, veuillez réessayer.")
