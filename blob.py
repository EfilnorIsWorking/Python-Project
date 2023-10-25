from constantes import *

class Blob :
    def __init__(self):
        self.energy = 100
        self.alive = True
        self.vitesse = 1

    def energyGain (self, v):
        if (v<energy_max):
            self.energy += v

    def death(self) :
        if self.energy<0 :
            self.alive = False


def birth_parth(bobMom):
    if bobMom.energy == energy_max :
       bob = blob()
       bob.energy = 50
       bobMom.energy -= 150
       return bob
