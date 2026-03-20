import pygame
from parametres import xbouton, ybouton, largeur_bouton, hauteur_bouton

# boutons du menu :
Jouer_bt = pygame.Rect(xbouton, ybouton - 70, largeur_bouton, hauteur_bouton)
Jouer_txt = "Appuyez pour jouer"

parametre_bt = pygame.Rect(xbouton, ybouton, largeur_bouton, hauteur_bouton)
parametre_txt = "paramètre"

rules_bt = pygame.Rect(xbouton, ybouton + 70, largeur_bouton, hauteur_bouton)
rules_txt = "Règles du jeu"

exit_bt = pygame.Rect(
    xbouton - 600, ybouton - 400, largeur_bouton // 3, hauteur_bouton // 2
)
exit_txt = "exit"

jcj_bt = pygame.Rect(0, 0, 240, 50)
jcj_txt = "Affrontez vous"


# boutons du mode de combat :

attaquer_bt = pygame.Rect(xbouton, ybouton, largeur_bouton, hauteur_bouton)
attaquer_txt = "Attaquer"

soin_bt = pygame.Rect(xbouton, ybouton + 70, largeur_bouton, hauteur_bouton)
soin_txt = "Soigner"

# boutons du menu de parametre :

facile_bt = pygame.Rect(xbouton - 500, ybouton, largeur_bouton, hauteur_bouton)
facile_txt = "Facile"


moyen_bt = pygame.Rect(xbouton - 500, ybouton + 70, largeur_bouton, hauteur_bouton)
moyen_txt = "Moyen"


difficile_bt = pygame.Rect(xbouton - 500, ybouton + 140, largeur_bouton, hauteur_bouton)
difficile_txt = "Difficile"

# bouton récompense niveau

more_force_bt = pygame.Rect(xbouton - 300, ybouton + 80, largeur_bouton, hauteur_bouton)
more_force_txt = "Force ++"


more_deplacement_bt = pygame.Rect(xbouton, ybouton + 80, largeur_bouton, hauteur_bouton)
more_deplacement_txt = "+1 deplacement"


more_life_bt = pygame.Rect(xbouton + 300, ybouton + 80, largeur_bouton, hauteur_bouton)
more_life_txt = "Life max +"
