from blob import *
from food import *
from constantes import *

def afficher_grille(taille, perso, bouffes):
    for ligne in range(taille):
        for colonne in range(taille):
            bonhomme = " "
            nourriture = " "

            #Affichage des Bobs si ils sont sur la case à dessiner
            for bob in perso:
                if (ligne == bob.x) and (colonne == bob.y):
                    nourriture = "B"

            #Affichage des Bobs si ils sont sur la case à dessiner
            for food in bouffes:
                if (ligne == food.x) and (colonne == food.y):
                    nourriture = "N"

            #Affichage de la case
            print("|""bonhomme}{nourriture}", end= "|")
        print("\n")

#Génération de nourriture
foods = []

for i in range(quantity_food):
    food = Food()
    foods.append(food)

#Génération de Bobs
bobs = []

for i in range(nbBob):
    bob = Blob()
    bobs.append(bob)

# Appeler la fonction pour afficher la grille
afficher_grille(taille_grille, bobs, foods)