import pygame
import parametres
import bouton
import fonction
import entities
from parametres import xbouton,ybouton,largeur_bouton,hauteur_bouton,taille_cell
screen = parametres.ecran

#UI Menu
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

# UI PLay
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
    
#UI Parametre
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
    pygame.draw.rect(screen,parametres.BLEU_FONCE if not parametres.facile_clicked else parametres.BLEU_CLAIR, bouton.facile_bt)
    fonction.afficher_texte(
        bouton.facile_txt,
        xbouton -500, ybouton,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    pygame.draw.rect(screen,parametres.BLEU_FONCE if not parametres.moyen_clicked else parametres.BLEU_CLAIR, bouton.moyen_bt)
    fonction.afficher_texte(
        bouton.moyen_txt,
        xbouton-500, ybouton+ 70,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    pygame.draw.rect(screen,parametres.BLEU_FONCE if not parametres.difficile_clicked else parametres.BLEU_CLAIR, bouton.difficile_bt)
    fonction.afficher_texte(
        bouton.difficile_txt,
        xbouton -500, ybouton + 140,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    fonction.afficher_texte(
        "Choisir la difficulté",
        xbouton -500, ybouton -70,
        largeur_bouton, hauteur_bouton,
        parametres.BLANC,
        parametres.taille_text
    )

#UI Rules
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
    
#UI Combat
def combat(screen):
    screen.fill(parametres.ROUGE_CLAIR)

    pygame.draw.rect(screen, parametres.BLEU_FONCE, bouton.exit_bt)
    fonction.afficher_texte(
        bouton.exit_txt,
        xbouton - 600, ybouton - 422,
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
        f"Tour de : {str(parametres.tour_de)}",
        xbouton, ybouton - 422,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    pygame.draw.rect(screen, parametres.ROUGE_FONCE, bouton.soin_bt)
    fonction.afficher_texte(
        bouton.soin_txt,
        xbouton, ybouton + 70,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )
    fonction.draw_health_bar(
        screen,
        x=xbouton, y=ybouton - 100,
        current=entities.j1.life,
        maximum=entities.j1.max_life,
        label="Joueur : "
    )
    fonction.draw_health_bar(
        screen,
        x=xbouton, y=ybouton - 150,
        current=entities.ennemi_en_combat.life,
        maximum=entities.ennemi_en_combat.max_life,
        label="Ennemi : "
    )
    fonction.draw_health_bar(
        screen,
        x=xbouton, y=ybouton - 75,
        current=entities.j1.armor,
        maximum=entities.j1.max_armor,
        label="Armure : ",
        color_override=(99, 179, 237)
    )
    fonction.afficher_texte(
        str(entities.j1.inventaire),
        xbouton, ybouton + 200,
        largeur_bouton, hauteur_bouton,
        parametres.NOIR,
        parametres.taille_text
    )

#UI Mort
def mort(screen):
    screen.fill(parametres.NOIR)

    fonction.afficher_texte(
        "Vous etes mort",
        xbouton, ybouton,
        largeur_bouton, hauteur_bouton,
        parametres.BLANC,
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