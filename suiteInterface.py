import pygame
import pygame_gui
import sys

pygame.init()
largeur, hauteur = 800, 600
window_surface = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("The Game Of Life")


background = pygame.Surface((800, 600))
#background = pygame.image.load('/home/ibighrman/PygameAssets-main/game.jpg')

manager = pygame_gui.UIManager((800, 600))

noir = (0, 0, 0)
blanc = (255, 255, 255)


police = pygame.font.Font(None, 36)


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

                        return True
                    elif 300 <= y <= 350:
                        pygame.quit()
                        sys.exit()

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("MENU DU JEU", largeur // 2, 100)
        pygame.draw.rect(window_surface, noir, (300, 200, 200, 50))
        afficher_texte("Start", largeur // 2, 225)
        pygame.draw.rect(window_surface, noir, (300, 300, 200, 50))
        afficher_texte("Quit", largeur // 2, 325)
        pygame.display.update()


def interface_jeu():
    jeu_en_cours = True
    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window_surface.fill((0, 0, 0))  
        afficher_texte("C'est parti!", largeur // 2, hauteur // 2)
        pygame.display.update()
        pygame.time.delay(4000)
        jeu_en_cours = False

if __name__ == "__main__":
    game_started = False
    while True:
        if not game_started:
            game_started = main_menu()
        else:
            interface_jeu()
