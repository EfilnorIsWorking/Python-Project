import os
import random
import math
import pygame
from PIL import Image
import array
import sys

taille_grille = 100

class Food(Entite):
    TYPE = "FOOD"
    def __init__(self):
        super().__init__()
        self.energy = 50
        self.has_been_eaten = False
