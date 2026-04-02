# ══ CHAPITRE : LISTES ══

# Création et accès
courses = ["pomme", "poire", "banane", "orange", "kiwi"]
print(courses[1])
courses[0] = "fraise"

# Parcourir une liste
for course in courses:
    print(course)

# Filtrer avec une condition
nombres = [3, 7, 2, 9, 1]
liste = []
for nombre in nombres:
    if nombre > 4:
        liste.append(nombre)
print("Nombres > 4 :", liste)

# len(), indices négatifs, slicing
scores = [12, 7, 19, 4, 15, 8]
print(len(scores))
print(scores[-1])
print(scores[-2])
print(scores[0:3])
print(scores[-3:])
print(scores[1:4])

# Exercice bilan — notes
notes = [12, 8, 15, 9, 17, 11]
valides = 0

for note in notes:
    if note >= 10:
        valides += 1
        print("Note", note, ": Valide")
    else:
        print("Note", note, ": Non valide")

print("Nombre de notes valides :", valides)
print("Moyenne des notes :", sum(notes) / len(notes))
