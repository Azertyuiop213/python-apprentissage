import random
random_number = random.randint(1, 100)
nombre_essais = 5
while nombre_essais > 0:
    guess = int(input("Devinez le nombre entre 1 et 100: "))    
    if random_number == guess:
        print("Félicitations! Vous avez deviné le nombre.")
        break
    nombre_essais -= 1
    print(f"Nombre d'essais restants: {nombre_essais}")
else:
    print("Dommage! Vous n'avez pas deviné le nombre.")