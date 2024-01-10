from blob import *
import time
from constantes import *
from grille import *  

bobs = []
foods = []
bobs = create_first_Blobs()


game_on = True
while game_on:

    foods = create_Food()
    
    
    for i in range(taille_grille):
        for j in range(taille_grille):
            for k in range(len(bobs)):
                if (i == bobs[k].x) and (j == bobs[k].y):
                    print(bobs[k].key, end="") 
            for f in range(len(foods)):
                if (i == foods[f].x) and (j == foods[f].y):
                    print("F", end="")
            
            print("\t", end="") 
        print("\n", end="")
    

    for k in range(len(bobs)):
        if bobs[k].alive == False:
            bobs.pop(k)
            break
        bobs[k].move()
        bobs[k].death()

        for f in range(len(foods)):
            if (bobs[k].x == foods[f].x) and (bobs[k].y == foods[f].y):
                bobs[k].eat(foods[f])
                foods.pop(f)
                break

        if bobs[k].energy > energy_max:
            bobs[k].energy = energy_max
        

           
    time.sleep(2)
    print("\033[H\033[J",end="")
    
