from constantes import *

class Food :
    def __init__(self):
        self.energyfood = energy_food
        self.pos_x = random.randint(0, 100)
        self.pos_y = random.randint(0, 100)
        self.appear = True
    def erase(self):
        if (self.energy = 0) :
            self.appear = False
        # Mettre l'énergie de toute la nourriture à zéro à la fin  de la journée, comme ça elle disparaisse
