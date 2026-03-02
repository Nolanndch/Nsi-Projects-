import pygame
import parametres
import random
import entities
from parametres import taille_cell
screen = parametres.ecran

class case():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.contenu = None

def creer_grille(n:int)->dict:
    dico = {}
    for y in range(n):
        for x in range(n):
            dico[(x,y)] = case(x,y)

    return dico

def afficher_grille(screen, dico):
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

        pygame.draw.rect(screen, parametres.BLEU_CLAIR, rect)
        pygame.draw.rect(screen, parametres.NOIR, rect, 1)  # contour

def afficher_inventaire(screen, inventaire):
    for cell in inventaire.values():
        rect = pygame.Rect(
            parametres.taille_inventaire * taille_cell,
            parametres.taille_inventaire * taille_cell,
            taille_cell,
            taille_cell
        )

        pygame.draw.rect(screen, parametres.GRIS_CLAIR, rect)
        pygame.draw.rect(screen, parametres.NOIR, rect, 1)


def afficher_joueur(screen, joueur):
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

def afficher_mob(screen, mob):
    largeur_grille = parametres.taille_grille * taille_cell
    hauteur_grille = parametres.taille_grille * taille_cell

    offset_x = (screen.get_width() - largeur_grille) // 2
    offset_y = (screen.get_height() - hauteur_grille) // 2

    rect = pygame.Rect(
        offset_x + mob.x * taille_cell,
        offset_y + mob.y * taille_cell,
        taille_cell,
        taille_cell
    )

    pygame.draw.rect(screen, mob.couleur, rect)

def afficher_texte(texte, x, y,largeur,hauteur,couleur,taille):
    if isinstance(texte,list):
        texte = ''.join(texte)
        
    rendu = taille.render(texte, True, couleur)
    screen.blit(rendu, ((x+largeur//2)-100, y+hauteur//2))

def placer_mob(grille):

    nb_enemie = parametres.wave_number * 1

    for i in range(nb_enemie):
        x = random.randint(0, parametres.taille_grille - 1)
        y = random.randint(0, parametres.taille_grille - 1)

        if grille[x,y].contenu == None:
            grille[x,y].contenu = entities.Mob(x,y)

def wave(grille):
    nb_enemies = 0
    for cell in grille.values():
        if cell.contenu != None:
            nb_enemies += 1

    if nb_enemies == 0:
        parametres.wave_number+=1
        placer_mob(grille)



def tour(): #choisi au hasard le premier qui attaque 
    tour= random.randint(0,1)

    if tour % 2 == 0 :
            parametres.tour_de = "Joueur"

    elif tour%2 != 0 :
            parametres.tour_de = "enemi"

def player_can_move(direction):

    if direction == "haut":
        return entities.j1.y - 1 >= 0
    
    if direction == "bas":
        return entities.j1.y + 1 < parametres.ymax + 1

    if direction == "gauche":
        return entities.j1.x - 1 >= 0

    if direction == "droite":
        return entities.j1.x + 1 < parametres.xmax + 1

def player_rencontre_mob(grille):
    contenu = grille[entities.j1.x,entities.j1.y].contenu

    if isinstance(contenu,entities.Mob):
        parametres.etat_du_jeu = "combat"
        entities.ennemi_en_combat = grille[entities.j1.x,entities.j1.y].contenu

def etat_precedent(loop):
    if parametres.etat_du_jeu == "menu":
        loop = False 
        pygame.quit()

    if parametres.etat_du_jeu == "play" or parametres.etat_du_jeu == "parametre" or parametres.etat_du_jeu == "rules":
        parametres.etat_du_jeu = "menu"

    if parametres.etat_du_jeu == "combat":
        parametres.etat_du_jeu = "play"