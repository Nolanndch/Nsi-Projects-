import pygame
import parametres
import random
import entities
from parametres import taille_cell
screen = parametres.ecran

class case(): #classe qui gere les cases et permet leur contenu
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.contenu = None

def creer_grille(n:int)->dict:
    #prend un entier en parametre et renvoie un dico de cases de n x n
    dico = {}
    for y in range(n):
        for x in range(n):
            dico[(x,y)] = case(x,y)

    return dico

def afficher_grille(screen, dico):
    #affiche la grille de jeu principale au centre de l'ecran
    largeur_grille = parametres.taille_grille * taille_cell
    hauteur_grille = parametres.taille_grille * taille_cell

    offset_x = (parametres.largeur_ecran - largeur_grille) // 2
    offset_y = (parametres.hauteur_ecran - hauteur_grille) // 2

    for cell in dico.values():
        rect = pygame.Rect(
            offset_x + cell.x * taille_cell,
            offset_y + cell.y * taille_cell,
            taille_cell,
            taille_cell
        )

        pygame.draw.rect(screen,parametres.BLEU_CLAIR, rect)
        pygame.draw.rect(screen, parametres.NOIR, rect, 1)

def afficher_joueur(screen, joueur):
    #affiche le joueur dans la grille de jeu principale
    largeur_grille = parametres.taille_grille * taille_cell
    hauteur_grille = parametres.taille_grille * taille_cell

    offset_x = (screen.get_width() - largeur_grille) // 2
    offset_y = (screen.get_height() - hauteur_grille) // 2

    rect = pygame.Rect(
        offset_x + joueur.x * taille_cell,
        offset_y + joueur.y * taille_cell,
        taille_cell,
        taille_cell
    )

    pygame.draw.rect(screen, joueur.couleur, rect)

def afficher_texte(texte, x, y,largeur,hauteur,couleur,taille):

    if isinstance(texte,list):
        texte = ''.join(texte)
        
    rendu = taille.render(texte, True, couleur)
    screen.blit(rendu, ((x+largeur//2)-100, y+hauteur//2))
    
def contenue_grille(grille):
    #place des mobs aleatoirement dans la grille de jeu principale
    #le nombre de mob varie selon la difficulté et la vague en cours

    if parametres.facile_clicked == False or parametres.moyen_clicked == False or parametres.difficile_clicked == False:
        difficulter = parametres.difficulter_defaut
    if parametres.facile_clicked == True :
        difficulter = 3
        parametres.nb_item_defaut = 5
    if parametres.moyen_clicked == True : 
        difficulter = 6
        parametres.nb_item_defaut = 4
    if parametres.difficile_clicked == True:
        difficulter = 9
        parametres.nb_item_defaut = 3
    
    nb_enemie = parametres.wave_number * difficulter
    
    for i in range(nb_enemie):
        x = random.randint(0, parametres.taille_grille - 1)
        y = random.randint(0, parametres.taille_grille - 1)

        if grille[x,y].contenu == None:
            grille[x,y].contenu = entities.Mob(x,y)
            
            
    for i in range(parametres.nb_item_defaut):
        x = random.randint(0, parametres.taille_grille - 1)
        y = random.randint(0, parametres.taille_grille - 1)

        if grille[x,y].contenu == None:
            grille[x,y].contenu = entities.soin


def tour():
    #choisi au hasard le premier qui attaque 
    tour= random.randint(0,1)

    if tour % 2 == 0 :
            parametres.tour_de = "Joueur"

    elif tour%2 != 0 :
            parametres.tour_de = "enemi"

def player_can_move(direction):
    #verifie si le joueur peut se deplacer
    if direction == "haut":
        return entities.j1.y - 1 >= 0
    
    if direction == "bas":
        return entities.j1.y + 1 < parametres.ymax + 1

    if direction == "gauche":
        return entities.j1.x - 1 >= 0

    if direction == "droite":
        return entities.j1.x + 1 < parametres.xmax + 1

def player_rencontre(grille):
    #verifie si le joueur se trouve sur la meme case qu'un mob ou un objet
    contenu = grille[entities.j1.x,entities.j1.y].contenu

    if isinstance(contenu,entities.Mob):
        parametres.etat_du_jeu = "combat"
        entities.ennemi_en_combat = grille[entities.j1.x,entities.j1.y].contenu

    elif isinstance(contenu,entities.Objet):
        if contenu == entities.armure :
            contenu.proteger()
            grille[entities.j1.x,entities.j1.y].contenu = None

        elif contenu == entities.soin :
            entities.j1.inventaire.append(contenu)
            grille[entities.j1.x,entities.j1.y].contenu = None


def etat_precedent(loop):
    #reviens a l'etat de jeu inferieur a celui actuel
    if parametres.etat_du_jeu == "menu":
        loop = False 
        pygame.quit()

    if parametres.etat_du_jeu == "play" or parametres.etat_du_jeu == "parametre" or parametres.etat_du_jeu == "rules" or parametres.etat_du_jeu == "mort":
        parametres.etat_du_jeu = "menu"

    if parametres.etat_du_jeu == "combat":
        parametres.etat_du_jeu = "play"

def reset_grille(grille):
    #nettoie la grille apres la mort du joueur et la rend prete a reprendre une partie
    for cell in grille.values():
        cell.contenu = None
    
    contenue_grille(grille)
    
def draw_health_bar(screen, x, y, current, maximum, width=200, height=18, label="", color_override=None):
    ratio = max(current / maximum, 0)

    if color_override:
        color = color_override        # ← couleur fixe (armure)
    elif ratio > 0.6:
        color = (34, 197, 94)         # Vert
    elif ratio > 0.3:
        color = (234, 179, 8)         # Jaune
    else:
        color = (239, 68, 68)         # Rouge

    pygame.draw.rect(screen, (60, 60, 60), (x, y, width, height), border_radius=5)
    if ratio > 0:
        pygame.draw.rect(screen, color, (x, y, int(width * ratio), height), border_radius=5)
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 2, border_radius=5)

    font = pygame.font.SysFont(None, 24)
    texte = font.render(f"{label}{current}/{maximum}", True, parametres.NOIR)
    screen.blit(texte, (x + width + 8, y))
    
def change_dificulty(dificulty,grille):
    
    if dificulty == "facile":
        parametres.facile_clicked = True
        parametres.moyen_clicked = False
        parametres.difficile_clicked = False
        
        
    if dificulty == "moyen":
        parametres.moyen_clicked = True
        parametres.facile_clicked = False
        parametres.difficile_clicked = False
        
    if dificulty == "difficile":
        parametres.difficile_clicked = True
        parametres.facile_clicked = False
        parametres.moyen_clicked = False
    
    
    reset_grille(grille)
    
def refill(grille):
    # replace des mobs et objets dans la grille si elle est vide
    mobs = 0
    for cell in grille.values():
        if isinstance(cell.contenu,entities.Mob):
            mobs +=1
    if mobs == 0:
        contenue_grille(grille)
        
def recompense(grille):
    if entities.ennemi_en_combat.life <= 0 :
        x = entities.ennemi_en_combat.x
        y = entities.ennemi_en_combat.y
        coord = (x+1,y)
        if coord in grille and grille[coord].contenu == None:
            grille[coord].contenu = random.choice([entities.soin, entities.armure])


def bouger_mob(grille):
    import pygame
    temps_actuel = pygame.time.get_ticks()

    # Pas encore le moment de bouger
    if temps_actuel - parametres.dernier_mouvement_mob < parametres.delai_mouvement_mob:
        return

    # On récupère tous les mobs
    mobs_a_bouger = [cell.contenu for cell in grille.values() if isinstance(cell.contenu, entities.Mob)]

    for enemi in mobs_a_bouger:

        # Si c'est le début du tour, on initialise le compteur de pas
        if enemi not in parametres.mobs_pas_restants:
            parametres.mobs_pas_restants[enemi] = parametres.deplacement_mob_max

        # S'il reste des pas à faire
        if parametres.mobs_pas_restants[enemi] > 0:
            # enlève de l'ancienne case
            grille[enemi.x, enemi.y].contenu = None
            # déplace d'une case
            enemi.se_deplacer(grille)
            #verifie si le mob est sur le joueur
            player_rencontre(grille)
            # place dans la nouvelle case
            grille[enemi.x, enemi.y].contenu = enemi
            # réduit le nombre de pas restants
            parametres.mobs_pas_restants[enemi] -= 1

    # Update du timer
    parametres.dernier_mouvement_mob = temps_actuel

    # Si tous les mobs ont fini leurs pas, reset pour le prochain tour et passe au joueur
    if all(p == 0 for p in parametres.mobs_pas_restants.values()):
        parametres.mobs_pas_restants.clear()
        parametres.tour_deplacement = "joueur"
