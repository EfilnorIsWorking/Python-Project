import pygame
import sys
import pygame_gui

pygame.init()
largeur, hauteur = 800, 600
window_surface = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("The Game Of Life")

background = pygame.Surface((800, 600))

noir = (0, 0, 0)
blanc = (255, 255, 255)
gris = (128, 128, 128)

police = pygame.font.Font(None, 36)


manager = pygame_gui.UIManager((800, 600))


capacite_bob = 1  

def afficher_texte(texte, x, y):
    texte_surface = police.render(texte, True, blanc)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (x, y)
    window_surface.blit(texte_surface, texte_rect)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 300 <= x <= 500:
                    if 200 <= y <= 250:
                        start_game()  
                    elif 400 <= y <= 450:
                        pygame.quit()
                        sys.exit()
                    elif 300 <= y <= 350:
                        options_menu()  

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("MENU DU JEU", largeur // 2, 100)
        pygame.draw.rect(window_surface, gris, (300, 200, 200, 50))
        afficher_texte("Start", largeur // 2, 225)
        pygame.draw.rect(window_surface, gris, (300, 300, 200, 50))  
        afficher_texte("Options", largeur // 2, 325)
        pygame.draw.rect(window_surface, gris, (300, 400, 200, 50))  
        afficher_texte("Quit", largeur // 2, 425)
        pygame.display.update()

def options_menu():
    options_menu_open = True
    while options_menu_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 300 <= x <= 500 and 400 <= y <= 450:
                    modifier_capacite_bob()  
                elif 300 <= x <= 500 and 500 <= y <= 550:
                    options_menu_open = False  

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("OPTIONS", largeur // 2, 100)
        
       
        afficher_texte("Capacité des bobs : " + str(capacite_bob), largeur // 2, 200)

      
        pygame.draw.rect(window_surface, gris, (250, 400, 300, 50))
        afficher_texte("Augmenter la capacité", largeur // 2, 425)
        
   
        pygame.draw.rect(window_surface, gris, (300, 500, 200, 50))
        afficher_texte("Retour", largeur // 2, 525)
        
        pygame.display.update()

def modifier_capacite_bob():
    
    global capacite_bob
    
    capacite_bob += 1

def start_game():
    
    jeu_en_cours = True
    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window_surface.fill((0, 0, 0))  
        afficher_texte("Le jeu a commencé", largeur // 2, hauteur // 2 - 50)
        afficher_texte("Capacité des bobs : " + str(capacite_bob), largeur // 2, hauteur // 2 + 50)
        pygame.display.update()
        pygame.time.delay(4000)
        jeu_en_cours = False

if __name__ == "__main__":
    game_started = False
    while True:
        if not game_started:
            game_started = main_menu()
        else:
            start_game()
