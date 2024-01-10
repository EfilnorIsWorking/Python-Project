import os
import random
import math
import array
import sys
from grille import *

taille_grille = 100

class Food(Entite):
    TYPE = "FOOD"
    def __init__(self):
        super().__init__()
        self.energy = 50
        self.has_been_eaten = False

def create_Food(): #création de la nourriture
    food = []
    for i in range(0, quantity_food):
        food.append(Food())
    return food #renvoie une liste de blobs qui devront être modélisés dans la grille

