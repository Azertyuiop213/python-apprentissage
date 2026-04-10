# ══ CHAPITRE : DICTIONNAIRES ══

# Création et accès
produit = {"nom": "orange", "prix": 0.5, "quantite": 10}
print(produit["nom"])
print(produit["prix"])
print(produit["quantite"])

# Modifier et ajouter
produit["prix"] = 0.8
produit["categorie"] = "fruit"
print(produit)

# Parcourir un dictionnaire
eleve = {"nom": "Elijak", "age": 17, "moyenne": 14}
for cle, valeur in eleve.items():
    print(cle, ":", valeur)
