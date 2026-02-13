import pygame
import parametres
import bouton
import UI
import fonction
from parametres import etat_du_jeu
screen = parametres.ecran

grille_jeu = fonction.creer_grille(parametres.taille_grille)
j1 = fonction.player(5, 6)
grille_jeu[j1.x, j1.y].contenu = j1

#gougougaga

loop = True
while loop :
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN :
            if etat_du_jeu == "menu":
                if event.key == pygame.K_ESCAPE :
                    loop = False
            else : 
                if event.key == pygame.K_ESCAPE :
                    etat_du_jeu = "menu"
                    
                if etat_du_jeu == "play" :
                    if event.key == pygame.K_UP:
                        j1.y-=1
                        grille_jeu[j1.x, j1.y].contenu = j1

                    if event.key == pygame.K_DOWN:
                        j1.y+=1
                        grille_jeu[j1.x, j1.y].contenu = j1

                    if event.key == pygame.K_LEFT:
                        j1.x-=1
                        grille_jeu[j1.x, j1.y].contenu = j1

                    if event.key == pygame.K_RIGHT:
                        j1.x+=1
                        grille_jeu[j1.x, j1.y].contenu = j1

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
            

    if etat_du_jeu == "menu" :
        UI.menu(screen)

    if etat_du_jeu == "play":
        UI.play(screen,grille_jeu,j1)
        
    if etat_du_jeu == 'parametre':
        UI.parametre(screen)

    if etat_du_jeu == 'rules':
        UI.rules(screen)
        
    pygame.display.flip()

pygame.quit()