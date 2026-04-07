# ══ CHAPITRE : POO ══

class Joueur:
    def __init__(self, nom, points):
        self.nom = nom
        self.points = points

    def afficher(self):
        print(f"Joueur : {self.nom} - Points : {self.points}")

    def ajouter_points(self, nombre):
        self.points += nombre
        print(f"{nombre} points ajoutés à {self.nom}. Total : {self.points}")


rex = Joueur("Rex", 10)
lucie = Joueur("Lucie", 20)
rex.afficher()
lucie.afficher()
rex.ajouter_points(5)
lucie.ajouter_points(15)

class Personnage:
    def __init__(self, nom, vie = 100):
        self.nom = nom
        self.vie = vie

    def afficher(self):
        print(f"Personnage : {self.nom} - Vie : {self.vie}")

class Guerrier(Personnage):
    def __init__(self, nom, vie = 100, force = 10):
        super().__init__(nom, vie)
        self.force = force

    def attaquer(self):
        print(f"{self.nom} attaque avec une force de {self.force}!")

arthur = Guerrier("Arthur", 120, 15)
arthur.afficher()
arthur.attaquer()
