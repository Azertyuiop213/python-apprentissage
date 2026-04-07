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
rex.afficher()
rex.ajouter_points(5)