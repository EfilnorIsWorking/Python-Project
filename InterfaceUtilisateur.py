import pygame
import sys
import os 
from pygame.locals import KEYDOWN, K_ESCAPE, K_RETURN, K_BACKSPACE
pygame.init()
#os.chdir("/home/adeleris/Desktop")

original_largeur, original_hauteur = 900, 450
largeur, hauteur = original_largeur, original_hauteur

window_surface = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("The Game Of Life")

original_image = pygame.image.load('background.jpg')
background = pygame.transform.scale(original_image, (largeur, hauteur))

instructions_image_path = 'background.jpg'
instructions_image = pygame.image.load(instructions_image_path)
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

musique = "start.mp3"
mario = "mario.mp3"

fullscreen = False

# Ajouter une variable globale pour le bouton "Luminosité"
bouton_luminosite_rect = pygame.Rect(largeur * 0.75, hauteur * 0.90, largeur * 0.22, hauteur * 0.09)

def afficher_texte(texte, x, y):
    texte_surface = police.render(texte, True, blanc)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (x, y)
    window_surface.blit(texte_surface, texte_rect)

# ...

def afficher_formulaire():
    labels = ["Nombre de bobs", "Energie bob", "Nombre de tick", "Vitesse initiale du bob", "Energie min perdue par tick"]
    valeurs = [0, 0, 0, 0, 0]

    font = pygame.font.Font(None, 36)
    input_rects = []
    color_active = pygame.Color('dodgerblue2')
    color_inactive = pygame.Color(vert)
    colors = [color_inactive, color_inactive, color_inactive, color_inactive, color_inactive]
    active = [False, False, False, False, False]
    texts = ["", "", "", "", ""]
    current_index = 0

    save_button_rect = pygame.Rect(largeur * 0.75, hauteur * 0.80, largeur * 0.22, hauteur * 0.09)
    next_button_rect = pygame.Rect(largeur * 0.75, hauteur * 0.90, largeur * 0.22, hauteur * 0.09)
    return_button_rect = pygame.Rect(largeur * 0.75, hauteur * 0.70, largeur * 0.22, hauteur * 0.09)


    for i in range(len(labels)):
        input_rects.append(pygame.Rect(largeur * 0.5, hauteur * (0.49 + 0.1 * i), largeur * 0.2, hauteur * 0.05))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                norm_x = x / largeur
                norm_y = y / hauteur

                for i in range(len(labels)):
                    if input_rects[i].collidepoint(event.pos):
                        active[i] = not active[i]
                        current_index = i
                    else:
                        active[i] = False

                if save_button_rect.collidepoint(event.pos):
                    # Save the values entered by the user
                    valeurs = [int(texts[i].strip()) if texts[i].strip().isdigit() else 0 for i in range(len(texts))]
                elif next_button_rect.collidepoint(event.pos):
                    # If "Next" button is clicked, move to the next interface
                    new_form_interface()
                elif return_button_rect.collidepoint(event.pos):
                    main_menu()

            elif event.type == KEYDOWN:
                if any(active):
                    if event.key == K_RETURN:
                        valeurs[current_index] = int(texts[current_index].strip()) if texts[current_index].strip().isdigit() else 0
                        active[current_index] = False
                    elif event.key == K_BACKSPACE:
                        texts[current_index] = texts[current_index][:-1]
                    else:
                        texts[current_index] += event.unicode
                elif event.key == K_ESCAPE:
                    main_menu()

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("OPTIONS", largeur // 2, 100)

        for i in range(len(labels)):
            pygame.draw.rect(window_surface, colors[i], input_rects[i], 2)

            label_surface = font.render(f"{labels[i]}:", True, noir)
            label_rect = label_surface.get_rect(topleft=(input_rects[i].x - label_surface.get_width() - 20, input_rects[i].centery - label_surface.get_height() // 2))
            window_surface.blit(label_surface, label_rect)

            txt_surface = font.render(texts[i] if active[i] else str(valeurs[i]), True, violet)
            width = max(200, txt_surface.get_width() + 10)
            input_rects[i].w = width
            window_surface.blit(txt_surface, (input_rects[i].x + 5, input_rects[i].y))
            pygame.draw.rect(window_surface, colors[i], input_rects[i], 2)

        # Draw and display the "Save" button
        pygame.draw.rect(window_surface, violet, save_button_rect)
        afficher_texte("Save", largeur * 0.85, int(hauteur * 0.85))

        # Draw and display the "Next" button
        pygame.draw.rect(window_surface, violet, next_button_rect)
        afficher_texte("Next", largeur * 0.85, int(hauteur * 0.95))


        pygame.draw.rect(window_surface, violet, return_button_rect)
        afficher_texte("Retour", largeur * 0.85, int(hauteur * 0.75))
        
        #pygame.display.update()
        pygame.display.flip()



def new_form_interface():
    labels = ["Masse du bob", "Rayon de perception du bob", "Point de mémoire de départ", "Energie perdue en mouvement"]
    valeurs = [0, 0, 0, 0]

    font = pygame.font.Font(None, 36)
    input_rects = []
    color_active = pygame.Color('dodgerblue2')
    color_inactive = pygame.Color(vert)
    colors = [color_inactive, color_inactive, color_inactive, color_inactive]
    active = [False, False, False, False]
    texts = ["", "", "", ""]
    current_index = 0

    save_button_rect = pygame.Rect(largeur * 0.75, hauteur * 0.80, largeur * 0.22, hauteur * 0.09)
    retour_button_rect = pygame.Rect(largeur * 0.75, hauteur * 0.70, largeur * 0.22, hauteur * 0.09)
    next_button_rect = pygame.Rect(largeur * 0.75, hauteur * 0.90, largeur * 0.22, hauteur * 0.09)

    for i in range(len(labels)):
        input_rects.append(pygame.Rect(largeur * 0.5, hauteur * (0.49 + 0.1 * i), largeur * 0.2, hauteur * 0.05))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()     
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(labels)):
                    if input_rects[i].collidepoint(event.pos):
                        active[i] = not active[i]
                        current_index = i
                    else:
                        active[i] = False
                if save_button_rect.collidepoint(event.pos):
                    # Save the values entered by the user
                    valeurs = [int(texts[i].strip()) if texts[i].strip().isdigit() else 0 for i in range(len(texts))]
                elif next_button_rect.collidepoint(event.pos):
                    # If "Next" button is clicked, move to the next interface
                    new_interface()
                elif retour_button_rect.collidepoint(event.pos):
                    # Retourner au menu principal
                    return "main_menu"

            elif event.type == pygame.KEYDOWN:
                if any(active):
                    if event.key == pygame.K_RETURN:
                        valeurs[current_index] = int(texts[current_index].strip()) if texts[current_index].strip().isdigit() else 0
                        active[current_index] = False
                    elif event.key == pygame.K_BACKSPACE:
                        texts[current_index] = texts[current_index][:-1]
                    else:
                        texts[current_index] += event.unicode

                elif event.key == pygame.K_ESCAPE:
                    return "main_menu"

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("OPTIONS", largeur // 2, 100)

        for i in range(len(labels)):
            pygame.draw.rect(window_surface, colors[i], input_rects[i], 2)

            label_surface = font.render(f"{labels[i]}:", True, noir)
            label_rect = label_surface.get_rect(topleft=(input_rects[i].x - label_surface.get_width() - 20, input_rects[i].centery - label_surface.get_height() // 2))
            window_surface.blit(label_surface, label_rect)

            txt_surface = font.render(texts[i] if active[i] else str(valeurs[i]), True, violet)
            width = max(200, txt_surface.get_width() + 10)
            input_rects[i].w = width
            window_surface.blit(txt_surface, (input_rects[i].x + 5, input_rects[i].y))
            pygame.draw.rect(window_surface, colors[i], input_rects[i], 2)

        # Dessiner et afficher le bouton "Save"
        pygame.draw.rect(window_surface, violet, save_button_rect)
        afficher_texte("Save", largeur * 0.85, int(hauteur * 0.85))

        # Dessiner et afficher le bouton "Retour"
        pygame.draw.rect(window_surface, violet, retour_button_rect)
        afficher_texte("Retour", largeur * 0.85, int(hauteur * 0.75))

        # Dessiner et afficher le bouton "Next"
        pygame.draw.rect(window_surface, violet, next_button_rect)
        afficher_texte("Next", largeur * 0.85, int(hauteur * 0.95))

        pygame.display.flip()

def new_interface():
    labels = ["Energie de naissance d'un bob", "Energie perdue par la mère", "Niveau énergie reproduction", "Energie perdue par les parents", "Energie de l'enfant"]
    valeurs = [0, 0, 0, 0, 0]

    font = pygame.font.Font(None, 36)
    input_rects = []
    color_active = pygame.Color('dodgerblue2')
    color_inactive = pygame.Color(vert)
    colors = [color_inactive, color_inactive, color_inactive, color_inactive, color_inactive]
    active = [False, False, False, False, False]
    texts = ["", "", "", "", ""]
    current_index = 0

    save_button_rect = pygame.Rect(largeur * 0.75, hauteur * 0.80, largeur * 0.22, hauteur * 0.09)
    retour_button_rect = pygame.Rect(largeur * 0.75, hauteur * 0.70, largeur * 0.22, hauteur * 0.09)

    for i in range(len(labels)):
        input_rects.append(pygame.Rect(largeur * 0.5, hauteur * (0.49 + 0.1 * i), largeur * 0.2, hauteur * 0.05))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()     
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                norm_x = x / largeur
                norm_y = y / hauteur

                for i in range(len(labels)):
                    if input_rects[i].collidepoint(event.pos):
                        active[i] = not active[i]
                        current_index = i
                    else:
                        active[i] = False
                if save_button_rect.collidepoint(event.pos):
                    # Save the values entered by the user
                    valeurs = [int(texts[i].strip()) if texts[i].strip().isdigit() else 0 for i in range(len(texts))]
                elif retour_button_rect.collidepoint(event.pos):
                    # Retourner au menu principal
                    return "main_menu"

            elif event.type == pygame.KEYDOWN:
                if any(active):
                    if event.key == pygame.K_RETURN:
                        valeurs[current_index] = int(texts[current_index].strip()) if texts[current_index].strip().isdigit() else 0
                        active[current_index] = False
                    elif event.key == pygame.K_BACKSPACE:
                        texts[current_index] = texts[current_index][:-1]
                    else:
                        texts[current_index] += event.unicode

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("OPTIONS", largeur // 2, 100)

        for i in range(len(labels)):
            pygame.draw.rect(window_surface, colors[i], input_rects[i], 2)

            label_surface = font.render(f"{labels[i]}:", True, noir)
            label_rect = label_surface.get_rect(topleft=(input_rects[i].x - label_surface.get_width() - 20, input_rects[i].centery - label_surface.get_height() // 2))
            window_surface.blit(label_surface, label_rect)

            txt_surface = font.render(texts[i] if active[i] else str(valeurs[i]), True, violet)
            width = max(200, txt_surface.get_width() + 10)
            input_rects[i].w = width
            window_surface.blit(txt_surface, (input_rects[i].x + 5, input_rects[i].y))
            pygame.draw.rect(window_surface, colors[i], input_rects[i], 2)

        #Dessiner et afficher le bouton "save"
        pygame.draw.rect(window_surface, violet, save_button_rect)
        afficher_texte("Save", largeur * 0.85, int(hauteur * 0.85))

        # Dessiner et afficher le bouton "Retour"
        pygame.draw.rect(window_surface, violet, retour_button_rect)
        afficher_texte("Retour", largeur * 0.85, int(hauteur * 0.75))
        

        pygame.display.flip()






def ajuster_positions_plein_ecran():
    global largeur, hauteur, background, instructions_image, bouton_luminosite_rect

    if fullscreen:
        largeur, hauteur = pygame.display.get_surface().get_size()
        bouton_luminosite_rect = pygame.Rect(largeur * 0.75, hauteur * 0.90, largeur * 0.22, hauteur * 0.09)
    else:
        largeur, hauteur = original_largeur, original_hauteur
        bouton_luminosite_rect = pygame.Rect(largeur * 0.75, hauteur * 0.90, largeur * 0.22, hauteur * 0.09)

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

    pygame.display.update()
    ajuster_positions_plein_ecran()

def gerer_redimensionnement(event):
    global largeur, hauteur
    largeur, hauteur = event.w, event.h
    ajuster_positions_plein_ecran()

def stopper_toutes_musiques():
    pygame.mixer.music.stop()

def rejouer_toutes_musiques():
    pygame.mixer.music.load(mario)
    pygame.mixer.music.play(-1)

def toggle_musique():
    if pygame.mixer.music.get_busy():
        stopper_toutes_musiques()
    else:
        rejouer_toutes_musiques()

pygame.mixer.music.load(mario)
pygame.mixer.music.play(-1)

# Fonction pour afficher le bouton "Luminosité"
def afficher_bouton_luminosite():
    pygame.draw.rect(window_surface, violet, bouton_luminosite_rect)

    afficher_texte("Luminosité", largeur * 0.85, int(hauteur * 0.95))

# Fonction pour afficher le bouton "Options"
def afficher_bouton_options():
    pygame.draw.rect(window_surface, violet, (largeur * 0.39, hauteur * 0.57, largeur * 0.22, hauteur * 0.09))
    afficher_texte("Options", largeur // 2, int(hauteur * 0.61))

# Fonction pour afficher le bouton "Quit"
def afficher_bouton_quit():
    pygame.draw.rect(window_surface, violet, (largeur * 0.39, hauteur * 0.69, largeur * 0.22, hauteur * 0.09))
    afficher_texte("Quitter", largeur // 2, int(hauteur * 0.73))

def menu_luminosite():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                norm_x = x / largeur
                norm_y = y / hauteur

                if 0.33 <= norm_x <= 0.67:
                    if 0.56 <= norm_y <= 0.65:
                        augmenter_luminosite()
                    elif 0.67 <= norm_y <= 0.76:
                        diminuer_luminosite()
                    elif 0.78 <= norm_y <= 0.87:
                        return  # Retour au menu principal

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("MENU LUMINOSITÉ", largeur // 2, 100)
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
                        afficher_bouton_options()
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
                elif bouton_luminosite_rect.collidepoint(x, y):  # Vérifier si le bouton "Luminosité" est cliqué
                    return "luminosite_menu"

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("GAME OF LIFE", largeur // 2, 100)
        pygame.draw.rect(window_surface, bleu, (largeur * 0.39, hauteur * 0.44, largeur * 0.22, hauteur * 0.09))
        afficher_texte("Démarrer", largeur // 2, int(hauteur * 0.48))
        afficher_bouton_options()
        afficher_bouton_luminosite()
        afficher_bouton_quit()
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
        "Appuyez sur 'Entrer' pour lancer le jeu"
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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                start_game()


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
                    if 0.78 <= norm_y <= 0.87:
                        options_menu_open = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return  # Retour au menu principal

        window_surface.fill((0, 0, 0))
        window_surface.blit(background, (0, 0))
        afficher_texte("OPTIONS", largeur // 2, 100)
        afficher_formulaire()  # Appelez la fonction pour afficher le formulaire
        pygame.draw.rect(window_surface, violet, (largeur * 0.33, hauteur * 0.78, largeur * 0.34, hauteur * 0.09))
        afficher_texte("Retour", largeur // 2, int(hauteur * 0.82))
        pygame.display.update()

def start_game():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(musique)
    pygame.mixer.music.play(-1)
    
    jeu_en_cours = True
    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                norm_x = x / largeur
                norm_y = y / hauteur

                # Ajout du mini-bouton "Retour au menu principal"
                if 0.75 <= norm_x <= 0.89 and 0.02 <= norm_y <= 0.09:
                    pygame.mixer.music.stop() 
                    rejouer_toutes_musiques()
                    main_menu()
                    
                

        window_surface.fill((0, 0, 0))
        afficher_texte("Le jeu a commencé", largeur // 2, hauteur // 2 - 50)

        pygame.draw.ellipse(window_surface, vert, (largeur * 0.75, hauteur * 0.02, largeur * 0.14, hauteur * 0.07))
        afficher_texte("Menu", int(largeur * 0.82), int(hauteur * 0.06))
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
            elif action == "luminosite_menu":
                menu_luminosite()
        else:
            start_game()

        ajuster_positions_plein_ecran() 
