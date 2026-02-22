import pygame
import parametres
import bouton
import fonction
import entities
from entities import j1, ennemi_en_combat
from parametres import xbouton,ybouton,largeur_bouton,hauteur_bouton,taille_cell,etat_du_jeu
screen = parametres.ecran

def menu(screen):
    screen.fill(parametres.BLEU)

    pygame.draw.rect(screen, parametres.BLEU_FONCE, bouton.Jouer_bt)
    fonction.afficher_texte(
        bouton.Jouer_txt,
        xbouton, ybouton - 70,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )

    pygame.draw.rect(screen, parametres.BLEU_FONCE, bouton.parametre_bt)
    fonction.afficher_texte(
        bouton.parametre_txt,
        xbouton + 40, ybouton,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    pygame.draw.rect(screen, parametres.BLEU_FONCE, bouton.rules_bt)
    fonction.afficher_texte(
        bouton.rules_txt,
        xbouton + 40, ybouton + 70,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    pygame.draw.rect(screen, parametres.BLEU_FONCE, bouton.exit_bt)
    fonction.afficher_texte(
        bouton.exit_txt,
        xbouton - 600, ybouton -422,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )


def play(screen,grille_jeu,joueur):
    screen.fill(parametres.VERT)
    fonction.afficher_grille(screen,grille_jeu)
    fonction.afficher_joueur(screen,joueur)

    for c in grille_jeu.values():
        if c.contenu != None:
            pygame.draw.circle(
                screen, c.contenu.couleur, (
                (screen.get_width() - parametres.taille_grille * taille_cell) // 2 + c.x * taille_cell + taille_cell // 2,
                (screen.get_height() - parametres.taille_grille * taille_cell) // 2 + c.y * taille_cell + taille_cell // 2
            ), taille_cell // 2 - 2)

    pygame.draw.rect(screen, parametres.BLEU_FONCE, bouton.exit_bt)
    fonction.afficher_texte(
        bouton.exit_txt,
        xbouton - 600, ybouton -422,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    fonction.afficher_texte(
        "vague "+str(parametres.wave_number),
        xbouton+50, ybouton - 422,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    
    
def parametre(screen):
    screen.fill(parametres.GRIS_FONCE)

    pygame.draw.rect(screen, parametres.BLEU_FONCE, bouton.exit_bt)
    fonction.afficher_texte(
        bouton.exit_txt,
        xbouton - 600, ybouton -422,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )

def rules(screen):
    screen.fill(parametres.JAUNE_CLAIR)

    pygame.draw.rect(screen, parametres.BLEU_FONCE, bouton.exit_bt)
    fonction.afficher_texte(
        bouton.exit_txt,
        xbouton - 600, ybouton -422,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )

def combat(screen):
    screen.fill(parametres.ROUGE_CLAIR)

    pygame.draw.rect(screen, parametres.BLEU_FONCE, bouton.exit_bt)
    fonction.afficher_texte(
        bouton.exit_txt,
        xbouton - 600, ybouton -422,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    pygame.draw.rect(screen, parametres.ROUGE_FONCE, bouton.attaquer_bt)
    fonction.afficher_texte(
        bouton.attaquer_txt,
        xbouton, ybouton,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    fonction.afficher_texte(
        f"vie restante : {str(entities.j1.life)}",
        xbouton, ybouton -100,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    fonction.afficher_texte(
        f"vie du mob : {str(entities.ennemi_en_combat.life)}",
        xbouton, ybouton -150,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )