class Personnage:
    def __init__(self, nom, vie, force):
        self.nom = nom
        self.vie = vie
        self.force = force

    def attaquer(self, cible):
        cible.vie -= self.force
        print(f"{self.nom} attaque  {cible.nom} — Vie restante : {cible.vie}")

    def vivant(self):
        return self.vie > 0

Personnage1 = Personnage("Guerrier", 100, 20)
Personnage2 = Personnage("Mage", 80, 25)
while Personnage1.vivant() and Personnage2.vivant():
    Personnage1.attaquer(Personnage2)
    if Personnage2.vivant():
        Personnage2.attaquer(Personnage1)
if Personnage1.vivant():
    print(f"{Personnage1.nom} a gagné !")
else:    print(f"{Personnage2.nom} a gagné !")


