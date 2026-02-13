import pygame
import parametres
import bouton
from parametres import xbouton,ybouton,largeur_bouton,hauteur_bouton,taille_cell,etat_du_jeu
screen = parametres.ecran

class player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = 50
        self.power = 10
        self.couleur = parametres.BLEU_FONCE

class case():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.couleur = parametres.NOIR

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

        pygame.draw.rect(screen, cell.couleur, rect)
        pygame.draw.rect(screen, parametres.NOIR, rect, 1)  # contour

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


def afficher_texte(texte, x, y,largeur,hauteur,couleur,taille):
    if isinstance(texte,list):
        texte = ''.join(texte)
        
    rendu = taille.render(texte, True, couleur)
    screen.blit(rendu, ((x+largeur//2)-100, y+hauteur//2))


pygame.init()