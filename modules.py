# ══ CHAPITRE : MODULES ══

import random

nombre_secret = random.randint(1, 10)
resultat = input("Devinez un nombre entre 1 et 10 : ")

if int(resultat) == nombre_secret:
    print("Bravo ! Vous avez deviné le nombre secret.")
else:
    print(f"Perdu ! Le nombre secret était {nombre_secret}.")