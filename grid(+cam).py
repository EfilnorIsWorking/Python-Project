import pygame, sys,random
from pygame.locals import QUIT

TILE_LARGEUR = 100
TILE_HAUTEUR =  50
LARGEUR_FENETRE = 1000
HAUTEUR_FENETRE = 1000
TAILLE_GRID = 100
x_start = LARGEUR_FENETRE/2-TILE_LARGEUR/2
y_start = 50

#Liste de liste
#grid = [[0] * TAILLE_GRID for _ in range(TAILLE_GRID)]
#Dictionnaire
grid = {(i, j): 0 for i in range(TAILLE_GRID) for j in range(TAILLE_GRID)}



#for i in range(TAILLE_GRID):
  #for j in range(TAILLE_GRID):
    #grid[i][j] = 0;

#representation terminale

tile_images = []


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

class CameraGroup(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.display_surface = pygame.display.get_surface()
    #self.water = water
    #self.sand = sand
    self.offset = pygame.math.Vector2()
    #self.sand_rect = self.sand.get_rect(midtop = (x_start,y_start))
    #self.water_rect = self.water.get_rect(midtop = (x_start,y_start))
    self.keyboard_speed = 50
    
    self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
    l = self.camera_borders['left']
    t = self.camera_borders['top']
    w = self.display_surface.get_size()[0]  - (self.camera_borders['left'] + self.camera_borders['right'])
    h = self.display_surface.get_size()[1]  - (self.camera_borders['top'] + self.camera_borders['bottom'])
    self.camera_rect = pygame.Rect(l,t,w,h)

    #zoom
    self.zoom = 1
    self.internal_surf_size = (150,150)
    self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
    self.int_rect = self.internal_surf.get_rect(center = (LARGEUR_FENETRE/2,HAUTEUR_FENETRE/2))
    self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
    

    self.grass = pygame.image.load("sprite/grass.png").convert_alpha()
  
  def keyboard_control(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      self.offset.y -= self.keyboard_speed
    elif keys[pygame.K_DOWN]:
      self.offset.y += self.keyboard_speed
    elif keys[pygame.K_RIGHT]:
      self.offset.x += self.keyboard_speed
    elif keys[pygame.K_LEFT]:
      self.offset.x -= self.keyboard_speed
    # Zoom in
    elif keys[pygame.K_a]:
        self.zoom += 10
    # Zoom out
    elif keys[pygame.K_b]:
        self.zoom -= 10

  def custom_draw(self):
    self.keyboard_control()
    self.internal_surf.fill('#71ddee')

    for i in range(TAILLE_GRID):
        for j in range(TAILLE_GRID):
          x_screen = x_start + (i - j) * TILE_LARGEUR/2
          y_screen = y_start + (i + j) * TILE_HAUTEUR/2
          grass_offset = (x_screen, y_screen) - self.offset
          #scaled_grass = pygame.transform.scale(self.grass, (int(TILE_LARGEUR * self.zoom),int(TILE_HAUTEUR * self.zoom)))
          #scaled_rect = scaled_grass.get_rect(topleft=grass_offset)
          #self.display_surface.blit(scaled_grass, scaled_rect)

          
          #zoomed_offset = grass_offset * self.zoom
          #self.internal_surf.blit(self.grass,grass_offset)
          
          #scaled_surf = pygame.transform.scale(self.internal_surf,self.internal_surface_size_vector * self.zoom)
          #scaled_rect = scaled_surf.get_rect(center = (LARGEUR_FENETRE/2,HAUTEUR_FENETRE/2))
          #self.display_surface.blit(scaled_surf,scaled_rect)
          self.display_surface.blit(self.grass,grass_offset)


pygame.init()
DISPLAYSURF = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
clock = pygame.time.Clock()
pygame.event.set_grab(True)

def draw_tile(surface,img,x,y):
  x_screen = x_start + (x-y) * TILE_LARGEUR/2
  y_screen = y_start + (x+y) * TILE_HAUTEUR/2
  surface.blit(img,(x_screen,y_screen))

def draw_grid(surface):
  #Pour liste
  #for i in range(TAILLE_GRID):
    #for j in range(TAILLE_GRID):
      #draw_tile(surface,tile_images[grid[i][j]],i,j)
  #Pour dictionnaire
  for (i, j), value in grid.items():
      draw_tile(surface, tile_images[value], i, j)

def draw():
  sand = pygame.image.load("sprite/sand.png").convert_alpha()
  water = pygame.image.load("sprite/water.png").convert_alpha()
  tile_images.append(pygame.image.load("sprite/grass.png").convert_alpha())
  tile_images.append(sand)
  tile_images.append(water)
  pygame.display.set_caption('Hello World!')
  draw_grid(DISPLAYSURF)


draw()
camera_group = CameraGroup()

while True:
  for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
            
  DISPLAYSURF.fill('#71ddee')
  camera_group.update()
  camera_group.custom_draw()
  pygame.display.update()
  clock.tick(60)