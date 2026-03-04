import pygame
from parametres import xbouton,ybouton,largeur_bouton,hauteur_bouton

#boutons du menu :
Jouer_bt= pygame.Rect(xbouton,ybouton - 70,largeur_bouton,hauteur_bouton)
Jouer_txt = "Appuyez pour jouer"

parametre_bt = pygame.Rect(xbouton,ybouton,largeur_bouton,hauteur_bouton, border_radius = 1000)
parametre_txt = "paramètre"

rules_bt = pygame.Rect(xbouton,ybouton + 70,largeur_bouton,hauteur_bouton, border_radius = 1000)
rules_txt = "Règles du jeu"

exit_bt = pygame.Rect(xbouton-600,ybouton-400,largeur_bouton//3,hauteur_bouton//2, border_radius = 1000)
exit_txt = "exit"

attaquer_bt = pygame.Rect(xbouton,ybouton,largeur_bouton,hauteur_bouton, border_radius = 1000)
attaquer_txt = "Attaquer"

soin_bt = pygame.Rect(xbouton,ybouton + 70,largeur_bouton,hauteur_bouton, border_radius = 1000)
soin_txt = "Soigner"

facile_bt = pygame.Rect(xbouton-500,ybouton,largeur_bouton,hauteur_bouton, border_radius = 1000)
facile_txt = "Facile"


moyen_bt = pygame.Rect(xbouton-500,ybouton + 70,largeur_bouton,hauteur_bouton, border_radius = 1000)
moyen_txt = "Moyen"


difficile_bt = pygame.Rect(xbouton-500,ybouton + 140,largeur_bouton,hauteur_bouton, border_radius = 1000)
difficile_txt = "Difficile"
