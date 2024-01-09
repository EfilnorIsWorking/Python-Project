import pygame
import requests 
import sys
from io import BytesIO

pygame.init()

original_largeur, original_hauteur = 900, 450
largeur, hauteur = original_largeur, original_hauteur

image_url = "https://github.com/EfilnorIsWorking/Python-Project/raw/main/git/background.jpg"
response = requests.get(image_url)
image_data = BytesIO(response.content)
original_image = pygame.image.load(image_data)
background = pygame.transform.scale(original_image, (largeur, hauteur))

window_surface = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("The Game Of Life")

#instructions_image_path = "https://github.com/EfilnorIsWorking/Python-Project/raw/main/git/background.jpg"
response = requests.get(image_url)
instructions_data = BytesIO(response.content)
instructions_image = pygame.image.load(instructions_data)
instructions_image = pygame.transform.scale(instructions_image, (largeur, hauteur))

police = pygame.font.Font(None, 36)

noir = (0, 0, 0)
blanc = (255, 255, 255)
gris = (128, 128, 128)
violet = (122, 55, 139)
bleu = (92, 172, 238)
vert = (164, 205, 50)

capacite_bob = 1
luminosite = 1.0

musique = "https://github.com/EfilnorIsWorking/Python-Project/raw/main/git/start.mp3"
mario = "https://github.com/EfilnorIsWorking/Python-Project/raw/main/git/mario.mp3"

fullscreen = False

def afficher_texte(texte, x, y):
    texte_surface = police.render(texte, True, blanc)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (x, y)
    window_surface.blit(texte_surface, texte_rect)

def ajuster_positions_plein_ecran():
    global largeur, hauteur, background, instructions_image

    if fullscreen:
        largeur, hauteur = pygame.display.get_surface().get_size()
    else:
        largeur, hauteur = original_largeur, original_hauteur

    background = pygame.transform.scale(original_image, (largeur, hauteur))
    instructions_image = pygame.transform.scale(instructions_image, (largeur, hauteur))

    bouton_largeur = 200
    bouton_hauteur = 40
    bouton_y = hauteur // 2 - bouton_hauteur // 2

    
    pygame.display.update()

def toggle_fullscreen():
    global fullscreen, largeur, hauteur, background
    fullscreen = not fullscreen

    if fullscreen:
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        largeur, hauteur = original_largeur, original_hauteur
        pygame.display.set_mode((largeur, hauteur))

    pygame.display.update()  # Mettez à jour la fenêtre avant d'ajuster les positions en mode plein écran
    ajuster_positions_plein_ecran()

def gerer_redimensionnement(event):
    global largeur, hauteur
    largeur, hauteur = event.w, event.h
    ajuster_positions_plein_ecran()


def stopper_toutes_musiques():
    pygame.mixer.music.stop()

def rejouer_toutes_musiques():
    pygame.mixer.music.load(BytesIO(requests.get(mario).content))
    pygame.mixer.music.play(-1)

def toggle_musique():
    if pygame.mixer.music.get_busy():
        stopper_toutes_musiques()
    else:
        rejouer_toutes_musiques()

pygame.mixer.music.load(BytesIO(requests.get(mario).content))
pygame.mixer.music.play(-1)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                norm_x = x / largeur
                norm_y = y / hauteur

                if 0.39 <= norm_x <= 0.61:
                    if 0.44 <= norm_y <= 0.53:
                        afficher_instructions()
                        return "start_game"
                    elif 0.57 <= norm_y <= 0.67:
                        return "options_menu"
                    elif 0.69 <= norm_y <= 0.79:
                        pygame.quit()
                        sys.exit()
                elif 0.75 <= norm_x <= 0.94 and 0.02 <= norm_y <= 0.12:
                    toggle_fullscreen()
                elif 0.75 <= norm_x <= 0.94 and 0.13 <= norm_y <= 0.31:
                    toggle_musique()
                elif 0.75 <= norm_x <= 0.94 and 0.32 <= norm_y <= 0.42:
                    rejouer_toutes_musiques()

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("GAME OF LIFE", largeur // 2, 100)
        pygame.draw.rect(window_surface, bleu, (largeur * 0.39, hauteur * 0.44, largeur * 0.22, hauteur * 0.09))
        afficher_texte("Démarrer", largeur // 2, int(hauteur * 0.48))
        pygame.draw.rect(window_surface, vert, (largeur * 0.39, hauteur * 0.57, largeur * 0.22, hauteur * 0.09))
        afficher_texte("Options", largeur // 2, int(hauteur * 0.61))
        pygame.draw.rect(window_surface, violet, (largeur * 0.39, hauteur * 0.69, largeur * 0.22, hauteur * 0.09))
        afficher_texte("Quitter", largeur // 2, int(hauteur * 0.73))
        pygame.draw.ellipse(window_surface, vert, (largeur * 0.75, hauteur * 0.02, largeur * 0.19, hauteur * 0.1))
        afficher_texte("Plein écran", int(largeur * 0.84), int(hauteur * 0.07))
        pygame.draw.ellipse(window_surface, vert, (largeur * 0.75, hauteur * 0.14, largeur * 0.19, hauteur * 0.1))
        afficher_texte("Musique", int(largeur * 0.84), int(hauteur * 0.19))
        pygame.display.update()



def afficher_instructions():
    instruction_text = [
        "Bienvenue dans le Game of Life!",
        "Le jeu consiste à...",
        # L'Ajout d'autres lignes d'instructions
        "",
        "Appuyez sur 'Echap' pour revenir au menu principal."
    ]

    instruction_font = pygame.font.Font(None, 24)

    instruction_screen = pygame.display.set_mode((largeur, hauteur))
    instruction_screen.blit(instructions_image, (0, 0))

    y_offset = 50
    for line in instruction_text:
        instruction_surface = instruction_font.render(line, True, noir)
        instruction_rect = instruction_surface.get_rect(center=(largeur // 2, y_offset))
        instruction_screen.blit(instruction_surface, instruction_rect)
        y_offset += 30

    pygame.display.flip()

    waiting_for_escape = True
    while waiting_for_escape:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                waiting_for_escape = False

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
                norm_x = x / largeur
                norm_y = y / hauteur

                if 0.33 <= norm_x <= 0.67:
                    if 0.44 <= norm_y <= 0.53:
                        modifier_capacite_bob()
                    elif 0.56 <= norm_y <= 0.65:
                        augmenter_luminosite()
                    elif 0.67 <= norm_y <= 0.76:
                        diminuer_luminosite()
                    elif 0.78 <= norm_y <= 0.87:
                        options_menu_open = False
                   
        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("OPTIONS", largeur // 2, 100)
        pygame.draw.rect(window_surface, vert, (largeur * 0.33, hauteur * 0.44, largeur * 0.34, hauteur * 0.09))
        afficher_texte("Augmenter Capacité", largeur // 2, int(hauteur * 0.48))
        pygame.draw.rect(window_surface, bleu, (largeur * 0.33, hauteur * 0.56, largeur * 0.34, hauteur * 0.09))
        afficher_texte("Augmenter Luminosité", largeur // 2, int(hauteur * 0.60))
        pygame.draw.rect(window_surface, bleu, (largeur * 0.33, hauteur * 0.67, largeur * 0.34, hauteur * 0.09))
        afficher_texte("Diminuer Luminosité", largeur // 2, int(hauteur * 0.71))
        pygame.draw.rect(window_surface, violet, (largeur * 0.33, hauteur * 0.78, largeur * 0.34, hauteur * 0.09))
        afficher_texte("Retour", largeur // 2, int(hauteur * 0.82))
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
    pygame.mixer.music.stop()
    pygame.mixer.music.load(BytesIO(requests.get(musique).content))
    pygame.mixer.music.play(-1)
    
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
            
            ajuster_positions_plein_ecran()  # Déplacez cet appel ici
        else:
            start_game()
