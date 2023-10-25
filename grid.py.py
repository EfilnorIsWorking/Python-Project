import pygame, sys,random
from pygame.locals import QUIT

TILE_LARGEUR = 100
TILE_HAUTEUR = 50
LARGEUR_FENETRE = 1000
HAUTEUR_FENETRE = 1000
TAILLE_GRID = 100
x_start = LARGEUR_FENETRE/2-TILE_LARGEUR/2
y_start = 50

grid = [[0] * TAILLE_GRID for _ in range(TAILLE_GRID)]


for i in range(TAILLE_GRID):
  for j in range(TAILLE_GRID):
    grid[i][j] = random.randint(0,2);

#representation terminale

tile_images = []

pygame.init()
clock = pygame.time.Clock()

def draw_tile(surface,img,x,y):
  x_screen = x_start + (x-y) * TILE_LARGEUR/2
  y_screen = y_start + (x+y) *TILE_HAUTEUR/2
  surface.blit(img,(x_screen,y_screen))

def draw_grid(surface):
  for i in range(TAILLE_GRID):
    for j in range(TAILLE_GRID):
      draw_tile(surface,tile_images[grid[i][j]],i,j)

def draw():
  DISPLAYSURF = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
  tile_images.append(pygame.image.load("sprite/grass.png"))
  tile_images.append(pygame.image.load("sprite/sand.png"))
  tile_images.append(pygame.image.load("sprite/water.png"))
  pygame.display.set_caption('Hello World!')
  draw_grid(DISPLAYSURF)
  #DISPLAYSURF.blit(tile_images[0],(LARGEUR_FENETRE/2-TILE_LARGEUR/2,50))
  #draw_tile(DISPLAYSURF,tile_images[0],0,0)
  #draw_tile(DISPLAYSURF,tile_images[0],1,0)
  #draw_tile(DISPLAYSURF,tile_images[0],2,0)
  #draw_tile(DISPLAYSURF,tile_images[0],0,1)
  #draw_tile(DISPLAYSURF,tile_images[0],1,1)
  #draw_tile(DISPLAYSURF,tile_images[0],2,1)
  #draw_tile(DISPLAYSURF,tile_images[0],0,2)
  #draw_tile(DISPLAYSURF,tile_images[0],1,2)
  #draw_tile(DISPLAYSURF,tile_images[0],2,2)

draw()
while True:
  for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
  pygame.display.update()
  clock.tick(60)