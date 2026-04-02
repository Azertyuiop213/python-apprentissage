# ══ CHAPITRE : FONCTIONS ══

# Paramètres par défaut
def afficher_note(note, matiere="Inconnue"):
    print(f"Votre note en {matiere} est : {note}")

afficher_note(15)
afficher_note(15, "Mathématiques")

# Retourner plusieurs valeurs
def stats(notes):
    return min(notes), max(notes), sum(notes) / len(notes)

minimum, maximum, moyenne = stats([12, 8, 15, 9, 17])
print("Minimum :", minimum)
print("Maximum :", maximum)
print("Moyenne :", moyenne)
