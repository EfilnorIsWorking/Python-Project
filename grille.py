import random

taille = 100

class Grid:
    def __init__(self, taille):
        self.lignes = taille
        self.colonnes = taille
        self.grid = [[0] * taille for _ in range(taille)]

    def remplir_grille(self, entite):
        for i in range(self.lignes):
            for j in range(self.colonnes):
                for entit in entite :
                    if (entit.x = i and entit.y = j):
                        self.grid[i][j].appends(entit)


    def case_adj(self, ligne, colonne):
        cases_adjacentes = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                nouvelle_ligne = ligne + i
                nouvelle_colonne = colonne + j
                if 0 <= nouvelle_ligne < self.lignes and 0 <= nouvelle_colonne < self.colonnes:
                    cases_adjacentes.append(self.grille[nouvelle_ligne][nouvelle_colonne])
        return cases_adjacentes


class Entite:
    def __init__(self):
        self.x = random.randint(0, taille_grille-1)
        self.y = random.randint(0, taille_grille-1)