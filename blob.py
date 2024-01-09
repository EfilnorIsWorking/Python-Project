import os
import random
import math
import array
import sys
from grille import *
from constantes import *


def get_cuberoot(x):
    if x < 0:
        x = abs(x)
        cube_root = pow(x, 1 / 3) * (-1)
    else:
        cube_root = pow(x, 1 / 3)

    return cube_root


class Blob(Entite):
    MUTATION_RAT = mutv
    def __init__(self, key, parent_name1, parent_name2):
        self.energy = 100
        self.energy_max = 200

        self.alive = True

        self.key = key
        self.parent_key1 = parent_name1.key
        self.parent_key2 = parent_name2.key

        if (self.parent_key1 != 0):
            self.vitesse = random(parent_name1.vitesse - MUTATION_RAT, parent_name1.vitesse + MUTATION_RAT)
            self.mass = random(parent_name1.mass - MUTATION_RAT, parent_name1.mass + MUTATION_RAT)
            self.perception += random.randint(-1, 1)
            self.position = parent_name1.position
        else :
            self.vitesse = 1
            self.mass = 1
            self.perception = 0
            super().__init__()

        self.size = get_cuberoot(self.mass)

    #def where_to_go(self, grille):
        #modifier de manière à observer ce qu'il y a dans les cases
        #move(self)


    def move(self):
        direction = random.randin(0,5)
        if direction == 0 :     #DOWN
            self.y += self.vitesse
            self.energy -= self.vitesse*self.vitesse

        elif direction == 1 :   #UP
            self.y -= self.vitesse
            self.energy -= self.vitesse*self.vitesse*self.mass

        elif direction == 2 :   #RIGHT
            self.x += self.vitesse
            self.energy -= self.vitesse*self.vitesse*self.mass

        elif direction == 3:    #LEFT
            self.x -= self.vitesse
            self.energy -= self.vitesse*self.vitesse*self.mass
        else :
            self.energy -= 0.5 #STAY
        #FAIRE BUFFER DIRECTIONNEL

    def energyGain (self, v):
        if (v<energy_max):
            self.energy += v

    def death(self) :
        if self.energy<0 :
            self.alive = False


def birth_parth(bobMom):
    if bobMom.energy == energy_max :
       bob = Blob()
       bob.energy = 50
       bobMom.energy -= 150
       return bob

def encounter_bobs(bob1, bob2): #se lance que lorsque Bob1 et Bob2 sont sur la même case
    if (bob1.mass/bob2.mass) < 2/3 :
        bob1.alive = False
        bob2.energy -= (1/2)*(bob1.mass/bob2.mass)*bob1.energy + (1/2)*bob1.energy
    if (bob2.mass/bob1.mass) < 2/3 :
        bob2.alive = False
        bob1.energy -= (1/2)*(bob2.mass/bob1.mass)*bob2.energy + (1/2)*bob2.energy
