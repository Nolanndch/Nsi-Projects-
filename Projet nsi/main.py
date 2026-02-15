import pygame
import parametres
import bouton
import UI
import fonction
from fonction import j1
from parametres import etat_du_jeu
screen = parametres.ecran
grille_jeu = fonction.creer_grille(parametres.taille_grille)
fonction.placer_mob(grille_jeu)

loop = True
while loop :
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN :
            if etat_du_jeu == "menu":
                if event.key == pygame.K_ESCAPE :
                    loop = False
            elif etat_du_jeu == "combat":
                if event.key == pygame.K_ESCAPE :
                    etat_du_jeu = "play"
            else : 
                if event.key == pygame.K_ESCAPE :
                    etat_du_jeu = "menu"
                    
                if etat_du_jeu == "play" :
                    if event.key == pygame.K_UP:
                        if grille_jeu[j1.x, j1.y - 1].contenu == None:
                            j1.y-=1
                        else:
                            etat_du_jeu = 'combat'

                    if event.key == pygame.K_DOWN:
                        if grille_jeu[j1.x, j1.y + 1].contenu == None:
                            j1.y+=1
                        else:
                            etat_du_jeu = 'combat'

                    if event.key == pygame.K_LEFT:
                        if grille_jeu[j1.x - 1, j1.y].contenu == None:
                            j1.x-=1
                        else:
                            etat_du_jeu = 'combat'

                    if event.key == pygame.K_RIGHT:
                        if grille_jeu[j1.x + 1, j1.y].contenu == None:
                            j1.x+=1
                        else:   
                            etat_du_jeu = 'combat'

        if event.type == pygame.MOUSEBUTTONDOWN:
            if etat_du_jeu == 'menu':
                if bouton.Jouer_bt.collidepoint(pygame.mouse.get_pos()):
                    etat_du_jeu = 'play'
                if bouton.parametre_bt.collidepoint(pygame.mouse.get_pos()):
                    etat_du_jeu = 'parametre'
                if bouton.rules_bt.collidepoint(pygame.mouse.get_pos()):
                    etat_du_jeu = 'rules'
                if bouton.exit_bt.collidepoint(pygame.mouse.get_pos()):
                    loop = False
            
            if etat_du_jeu == 'play':
                if bouton.exit_bt.collidepoint(pygame.mouse.get_pos()):
                    etat_du_jeu = 'menu'

            if etat_du_jeu == 'parametre':
                if bouton.exit_bt.collidepoint(pygame.mouse.get_pos()):
                    etat_du_jeu = 'menu'
            
            if etat_du_jeu == 'rules':
                if bouton.exit_bt.collidepoint(pygame.mouse.get_pos()):
                    etat_du_jeu = 'menu'   

            if etat_du_jeu == 'combat':

                if bouton.exit_bt.collidepoint(pygame.mouse.get_pos()):
                    etat_du_jeu = 'play' 

                if bouton.attaquer_bt.collidepoint(pygame.mouse.get_pos()):
                    for c in grille_jeu.values():
                        if (c.x,c.y) == (j1.x,j1.y) :
                            j1.attaquer(c.contenu)

    if etat_du_jeu == "menu" :
        UI.menu(screen)

    if etat_du_jeu == "play":
        UI.play(screen,grille_jeu,j1)
        
    if etat_du_jeu == 'parametre':
        UI.parametre(screen)

    if etat_du_jeu == 'rules':
        UI.rules(screen)

    if etat_du_jeu == 'combat':
        UI.combat(screen)
        
    pygame.display.flip()

pygame.quit()