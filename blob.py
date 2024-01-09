import os
from random import *
import math
import array
import sys
from grille import *
from constantes import *
from food import *

#problèmes : gérer l'aspect aléatoire des clés des blobs, peut-être créer une variable qui sera incrémentée à chaque création de blob

def get_cuberoot(x):
    if x < 0:
        x = abs(x)
        cube_root = pow(x, 1 / 3) * (-1)
    else:
        cube_root = pow(x, 1 / 3)

    return cube_root


class Blob(Entite):

    def __init__(self, key, parent_name1, parent_name2): #initialisation des blobs
        self.energy = 100
        self.energy_max = 200
        self.perception = 0
        self.alive = True

        self.key = key

        self.buffer_vitesse = 0.0

        if (parent_name1 == None) and (parent_name2 == None): #si le blob n'a pas de parents
            self.parent_key1 = 0
            self.parent_key2 = 0
        else : #si le blob a des parents
            self.parent_key1 = parent_name1
            self.parent_key2 = parent_name2



        if (self.parent_key1 != 0): #si le blob a au moins un parent
            self.vitesse = uniform(parent_name1.vitesse - mutv, parent_name1.vitesse + mutv)
            self.mass = uniform(parent_name1.mass - mutv, parent_name1.mass + mutv)
            self.perception += randint(-1, 1)
            self.x = parent_name1.x
            self.y = parent_name1.x
        else : #si le blob n'a pas de parents
            self.vitesse = 1
            self.mass = 1
            self.perception = 0
            super().__init__()

        self.size = get_cuberoot(self.mass)

    #def where_to_go(self, grille):
        #modifier de manière à observer ce qu'il y a dans les cases
        #move(self)

    def eat(self, food): #manger de la nourriture
        self.energy += food.energy
        food.has_been_eaten = True

    def move(self): #déplacement des blobs
        direction = randint(0,5)
        if direction == 0 : #DOWN
            self.buffer_vitesse += self.vitesse
            self.y += int(self.buffer_vitesse)
            self.energy -= self.vitesse*self.vitesse
            self.buffer_vitesse -= int(self.buffer_vitesse)

        elif direction == 1 :   #UP
            self.buffer_vitesse += self.vitesse
            self.y -= int(self.buffer_vitesse)
            self.energy -= self.vitesse*self.vitesse*self.mass

        elif direction == 2 :   #RIGHT
            self.buffer_vitesse += self.vitesse
            self.x += int(self.buffer_vitesse)
            self.energy -= self.vitesse*self.vitesse*self.mass

        elif direction == 3:    #LEFT
            self.buffer_vitesse += self.vitesse
            self.x -= int(self.buffer_vitesse)
            self.energy -= self.vitesse*self.vitesse*self.mass
        else :
            self.energy -= 0.5 #STAY

    def energyGain (self, v): #gain d'énergie
        if (v<energy_max):
            self.energy += v

    def death(self) : #mort des blobs
        if self.energy<0 :
            self.alive = False


def birth_parth(bobMom): #création d'un blob par parthénogénèse
    if bobMom.energy == energy_max :
       bob = Blob(key = 10, parent_name1 = bobMom, parent_name2 = None)
       bob.energy = 50
       bobMom.energy -= 150
       return bob
    
def birth(bobMom, bobDad): #création d'un blob par reproduction
    if bobMom.energy == sex_energy_needed and bobDad.energy == sex_energy_needed :
        bob = Blob(key = 10, parent_name1 = bobMom, parent_name2 = bobDad)
        bob.energy = child_sex_energy
        bobMom.energy -= parents_sex_energy
        bobDad.energy -= parents_sex_energy
        return bob

def encounter_bobs(bob1, bob2): #se lance que lorsque Bob1 et Bob2 sont sur la même case
    if (bob1.mass/bob2.mass) < 2/3 :
        bob1.alive = False
        bob2.energy -= (1/2)*(bob1.mass/bob2.mass)*bob1.energy + (1/2)*bob1.energy
    if (bob2.mass/bob1.mass) < 2/3 :
        bob2.alive = False
        bob1.energy -= (1/2)*(bob2.mass/bob1.mass)*bob2.energy + (1/2)*bob2.energy


def create_first_Blobs(): #création des premiers blobs
    bobs = []
    for i in range(0, nbBob):
        bob = Blob(key = i, parent_name1 = None, parent_name2 = None)
        bobs.append(bob)
    return bobs #utiliser avec grille.remplir_grille(bobs)gv
