import pygame
import sys

pygame.init()

largeur, hauteur = 900, 450
window_surface = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("The Game Of Life")

original_image = pygame.image.load('/home/ibighrman/PygameAssets-main/background.jpg')
background = pygame.transform.scale(original_image, (largeur, hauteur))

police = pygame.font.Font(None, 36)

noir = (0, 0, 0)
blanc = (255, 255, 255)
gris = (128, 128, 128)

capacite_bob = 1
luminosite = 1.0

musique = pygame.mixer.Sound("/home/ibighrman/projet_python/musique.mp3")

fullscreen = False

def afficher_texte(texte, x, y):
    texte_surface = police.render(texte, True, blanc)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (x, y)
    window_surface.blit(texte_surface, texte_rect)

def ajuster_positions_plein_ecran():
    global largeur, hauteur, background

    # Calculer les nouvelles dimensions de l'écran
    largeur, hauteur = pygame.display.get_surface().get_size()

    # Redimensionner l'image de fond
    background = pygame.transform.scale(original_image, (largeur, hauteur))

def toggle_fullscreen():
    global fullscreen, largeur, hauteur, background
    fullscreen = not fullscreen
    pygame.display.toggle_fullscreen()
    if fullscreen:
        ajuster_positions_plein_ecran()
    else:
        largeur, hauteur = 900, 450
        pygame.display.set_caption("The Game Of Life")
        background = pygame.transform.scale(original_image, (largeur, hauteur))

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 350 <= x <= 550:
                    if 200 <= y <= 240:
                        return "start_game"
                    elif 260 <= y <= 300:
                        return "options_menu"
                    elif 320 <= y <= 360:
                        pygame.quit()
                        sys.exit()
                elif 600 <= x <= 700 and 10 <= y <= 50:
                    toggle_fullscreen()

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("GAME OF LIFE", largeur // 2, 100)
        pygame.draw.rect(window_surface, gris, (350, 200, 200, 40))
        afficher_texte("Start", largeur // 2, 220)
        pygame.draw.rect(window_surface, gris, (350, 260, 200, 40))
        afficher_texte("Options", largeur // 2, 280)
        pygame.draw.rect(window_surface, gris, (350, 320, 200, 40))
        afficher_texte("Quit", largeur // 2, 340)

        # Bouton Plein écran
        pygame.draw.rect(window_surface, gris, (600, 10, 200, 40))
        afficher_texte("Plein écran", 700, 30)

        pygame.display.update()

def options_menu():
    global luminosite, capacite_bob

    options_menu_open = True
    while options_menu_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 300 <= x <= 600:
                    if 200 <= y <= 240:
                        modifier_capacite_bob()
                    elif 250 <= y <= 290:
                        augmenter_luminosite()
                    elif 300 <= y <= 340:
                        diminuer_luminosite()
                    elif 350 <= y <= 390:
                        options_menu_open = False

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("OPTIONS", largeur // 2, 100)
        pygame.draw.rect(window_surface, gris, (300, 200, 300, 40))
        afficher_texte("Augmenter Capacité", largeur // 2, 220)
        pygame.draw.rect(window_surface, gris, (300, 250, 300, 40))
        afficher_texte("Augmenter Luminosité", largeur // 2, 270)
        pygame.draw.rect(window_surface, gris, (300, 300, 300, 40))
        afficher_texte("Diminuer Luminosité", largeur // 2, 320)
        pygame.draw.rect(window_surface, gris, (300, 350, 300, 40))
        afficher_texte("Retour", largeur // 2, 370)
        pygame.display.update()

def augmenter_luminosite():
    global luminosite
    luminosite += 0.1
    pygame.display.set_gamma(luminosite)

def diminuer_luminosite():
    global luminosite
    luminosite -= 0.1
    pygame.display.set_gamma(luminosite)

def modifier_capacite_bob():
    global capacite_bob
    capacite_bob += 1

def start_game():
    pygame.mixer.Sound.play(musique)
    jeu_en_cours = True
    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window_surface.fill((0, 0, 0))
        afficher_texte("Le jeu a commencé", largeur // 2, hauteur // 2 - 50)
        pygame.display.update()

if __name__ == "__main__":
    game_started = False
    while True:
        if not game_started:
            action = main_menu()
            if action == "start_game":
                game_started = True
                start_game()
            elif action == "options_menu":
                options_menu()
        else:
            start_game()
