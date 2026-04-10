# ══ CHAPITRE : FICHIERS ══

# Écriture
with open("notes.txt", "w") as f:
    f.write("Elijak\ntruc\nbidule")

# Lecture
with open("notes.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())

# Exercice — saisie utilisateur + écriture + lecture
prenoms = []
for i in range(3):
    prenom = input("Entrez un prénom : ")
    prenoms.append(prenom)

with open("prenoms.txt", "w") as f:
    for prenom in prenoms:
        f.write(prenom + "\n")

with open("prenoms.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
