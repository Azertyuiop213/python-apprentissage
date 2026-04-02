# ══ EXERCICE BILAN ══

prenom = input("Quel est votre prénom ? ")
age = input("Quel est votre âge ? ")
personne = {"prénom": prenom, "âge": age}

if int(age) >= 18:
    print(f"Bonjour {prenom}, vous êtes majeur.")
else:
    print(f"Bonjour {prenom}, vous êtes mineur.")

notes = [10, 15, 12, 8, 20]
moyenne = sum(notes) / len(notes)
print(f"Votre moyenne est de {moyenne}")
if moyenne >= 10:
    print("Mention passable")
else:
    print("Ajourné")
