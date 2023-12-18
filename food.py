import os
import random
import math
import pygame
from PIL import Image
import array
import sys

taille_grille = 100

class Food:
    TYPE = "FOOD"
    def __init__(self):
        self.x = random.randint(0, taille_grille - 1)
        self.y = random.randint(0, taille_grille - 1)
        self.energy = 50
        self.has_been_eaten = False
