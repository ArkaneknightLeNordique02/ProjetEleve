# Demande des informations à l'utilisateur
nom = input("Entrez le nom de l'étudiant : ")
matière = input("Entrez le nom de la matière : ")
note = float(input("Entrez la note obtenue : "))
while True:
        if ( note > 10) or (note < 0):
            print("saisissez une note inferieure ou egale a 10")
            note=float(input("Quelle est votre note dans ce cours:"))
        else:
            
            break
# Affichage des informations saisies
print(f"Nom de l'étudiant : {nom}")
print(f"Matière : {matière}")
print(f"Note : {note}")
