prenoms = []
for i in range(3):
    prenom = input ("Entrez un prénom : ")
    prenoms.append(prenom)

with open("prenoms.txt", "w") as f:
    for prenom in prenoms:
        f.write(prenom + "\n")

with open("prenoms.txt", "r") as f:
    for line in f:
        print(line.strip())
        