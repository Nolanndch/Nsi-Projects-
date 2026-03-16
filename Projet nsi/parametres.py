import pygame

pygame.init()

# Tous les settings du jeu :

ecran = pygame.display.set_mode()
largeur_ecran, hauteur_ecran = ecran.get_size()
taille_titres = pygame.font.SysFont(None, 40)
taille_text = pygame.font.SysFont(None, 30)
largeur_bouton = 250
hauteur_bouton = 50
xbouton = (largeur_ecran - largeur_bouton) // 2
ybouton = (hauteur_ecran - hauteur_bouton) // 2
taille_cell = 50
taille_grille = 40

etat_du_jeu = "menu"
wave_number = 1
tour_de = None

tour_deplacement = "joueur"
deplacement_joueur_max = 6
deplacement_mob_max = 4
nb_deplacement = 0

xmin = 0
xmax = taille_grille - 1
ymin = 0
ymax = taille_grille - 1

dernier_mouvement = 0
dernier_mouvement_mob = 0
delai_mouvement_mob = 1000
mobs_pas_restants = {}

delai_mouvement = 150
dernier_changement = 0
delai_combat = 800

facile_clicked = False
moyen_clicked = False
difficile_clicked = False
difficulter_defaut = 3
nb_item_defaut = 5

# Couleurs :

NOIR = (0, 0, 0)
GRIS_FONCE = (30, 30, 30)
GRIS = (60, 60, 60)
GRIS_CLAIR = (120, 120, 120)
BLANC = (230, 230, 230)
ROUGE_FONCE = (120, 40, 40)
ROUGE = (200, 80, 80)
ROUGE_CLAIR = (230, 120, 120)
VERT_FONCE = (40, 120, 80)
VERT = (80, 200, 120)
VERT_CLAIR = (140, 230, 180)
BLEU_FONCE = (40, 80, 120)
BLEU = (100, 150, 220)
BLEU_CLAIR = (160, 200, 240)
JAUNE_FONCE = (160, 130, 50)
JAUNE = (230, 180, 70)
JAUNE_CLAIR = (250, 220, 150)
VIOLET_FONCE = (90, 60, 120)
VIOLET = (150, 110, 190)
VIOLET_CLAIR = (200, 160, 230)
MARRON = (120, 90, 60)
ORANGE = (220, 140, 60)
CYAN = (80, 200, 200)
