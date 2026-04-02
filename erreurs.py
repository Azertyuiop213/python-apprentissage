try:
    nombre = input("Entrez un nombre : ")
    resultat = 100/float(nombre)
    print(resultat)
except ValueError:
    print("Vous devez entrer un nombre valide.")
except ZeroDivisionError:
    print("Le nombre ne peut pas être zéro.")