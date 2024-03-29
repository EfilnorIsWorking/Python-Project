import os
from random import *
import math
import array
import sys
from grille import *
from constantes import *
from food import *


global_key = 0 #clé différente pour chaque blob, puisque incrémentée à chaque création de blob

def get_cuberoot(x):
    if x < 0:
        x = abs(x)
        cube_root = pow(x, 1 / 3) * (-1)
    else:
        cube_root = pow(x, 1 / 3)
    return cube_root


class Blob(Entite):

    def __init__(self, key, parent_name1, parent_name2): #initialisation des blobs
        self.energy = energy_normale
        self.energy_max = energy_max
        self.perception = perception_normale
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
        else : #si le blob n'a pas de parents ses options sont normales 
            self.vitesse = vitesse_normale
            self.mass = masse_normale
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
            if (self.y > taille_grille-1):
                self.y = taille_grille-1
            self.energy -= self.vitesse*self.vitesse
            self.buffer_vitesse -= int(self.buffer_vitesse)

        elif direction == 1 :   #UP
            self.buffer_vitesse += self.vitesse
            self.y -= int(self.buffer_vitesse)
            if (self.y < 0):
                self.y = 0
            self.energy -= self.vitesse*self.vitesse*self.mass

        elif direction == 2 :   #RIGHT
            self.buffer_vitesse += self.vitesse
            self.x += int(self.buffer_vitesse)
            if (self.x > taille_grille-1):
                self.x = taille_grille-1
            self.energy -= self.vitesse*self.vitesse*self.mass

        elif direction == 3:    #LEFT
            self.buffer_vitesse += self.vitesse
            self.x -= int(self.buffer_vitesse)
            if (self.x < 0):
                self.x = 0
            self.energy -= self.vitesse*self.vitesse*self.mass
        else :
            self.energy -= 0.5 #STAY

    def death(self) : #mort des blobs
        if self.energy<0 :
            self.alive = False


def birth_parth(bobMom): #création d'un blob par parthénogénèse
    if bobMom.energy == energy_max :
       bob = Blob(global_key, parent_name1 = bobMom, parent_name2 = None)
       bob.energy = 50
       bobMom.energy -= 150
       global_key += 1
       return bob
    
def birth(bobMom, bobDad): #création d'un blob par reproduction
    if bobMom.energy == sex_energy_needed and bobDad.energy == sex_energy_needed :
        bob = Blob(global_key, parent_name1 = bobMom, parent_name2 = bobDad)
        bob.energy = child_sex_energy
        bobMom.energy -= parents_sex_energy
        bobDad.energy -= parents_sex_energy
        global_key += 1
        return bob

def battle_of_bobs(bob1, bob2): #se lance que lorsque Bob1 et Bob2 sont sur la même case
    if (bob1.mass/bob2.mass) < 2/3 :
        bob1.alive = False
        bob2.energy -= (1/2)*(bob1.mass/bob2.mass)*bob1.energy + (1/2)*bob1.energy
    if (bob2.mass/bob1.mass) < 2/3 :
        bob2.alive = False
        bob1.energy -= (1/2)*(bob2.mass/bob1.mass)*bob2.energy + (1/2)*bob2.energy


def create_first_Blobs(): #création des premiers blobs après le premier tick, ils ne seront que créer par parthénogénèse/reproduction
    global global_key
    bobs = []
    for i in range(0, nbBob):
        bob = Blob(global_key, parent_name1 = None, parent_name2 = None)
        bobs.append(bob)
        global_key += 1
    return bobs #renvoie une liste de blobs qui devront être modélisés dans la grille

