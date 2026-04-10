# ══ CHAPITRE : GESTION DES ERREURS ══

try:
    nombre = input("Entrez un nombre : ")
    resultat = 100 / float(nombre)
    print(f"100 / {nombre} = {resultat}")
except ValueError:
    print("Erreur : entrez un nombre valide.")
except ZeroDivisionError:
    print("Erreur : division par zéro impossible.")