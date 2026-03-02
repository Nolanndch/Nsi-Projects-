import pygame
import parametres
import bouton
import UI
import fonction
import entities
from parametres import etat_du_jeu
from fonction import player_can_move
screen = parametres.ecran
grille_jeu = fonction.creer_grille(parametres.taille_grille)
inventaire = fonction.creer_grille(parametres.taille_inventaire)
fonction.placer_mob(grille_jeu)
fonction.tour()

clock = pygame.time.Clock()

loop = True
while loop :
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN :#les verifs des click clavier

            if etat_du_jeu == "menu":
                if event.key == pygame.K_ESCAPE :
                    loop = False

            elif etat_du_jeu == "combat":
                if event.key == pygame.K_ESCAPE :
                    etat_du_jeu = "play"

                if event.key == pygame.K_a :
                    if entities.ennemi_en_combat != None and parametres.tour_de == "Joueur" :
                        entities.j1.attaquer(entities.ennemi_en_combat)
                        parametres.tour_de = 'enemi'
            else :
                if event.key == pygame.K_ESCAPE :
                    etat_du_jeu = "menu"

        if event.type == pygame.MOUSEBUTTONDOWN: #les verifs des boutons
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

                if entities.ennemi_en_combat != None and parametres.tour_de == "Joueur" : #verfifie le tour du joueur 
                    
                    if bouton.attaquer_bt.collidepoint(pygame.mouse.get_pos()):
                        entities.j1.attaquer(entities.ennemi_en_combat)
                        parametres.tour_de = "enemi"
                        parametres.dernier_changement = pygame.time.get_ticks()
                    
                    if bouton.soin_bt.collidepoint(pygame.mouse.get_pos()):
                        entities.j1.soigner(5)
                        parametres.tour_de = "enemi"
                        parametres.dernier_changement = pygame.time.get_ticks()

                    

    if entities.j1.life <= 1 :
        etat_du_jeu = "mort"

    if etat_du_jeu == "menu" :
        UI.menu(screen)

    if etat_du_jeu == "play":
        UI.play(screen,grille_jeu,entities.j1,inventaire)
        fonction.wave(grille_jeu)
        fonction.player_rencontre_mob(grille_jeu)

        clock.tick(60)  # limite à 60 FPS

        temps_actuel = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        if temps_actuel - parametres.dernier_mouvement > parametres.delai_mouvement:

            # DROITE
            if keys[pygame.K_RIGHT]:
                if player_can_move("droite"):
                    entities.j1.x += 1
                    parametres.dernier_mouvement = temps_actuel

            # GAUCHE
            elif keys[pygame.K_LEFT]:
                if player_can_move("gauche"):
                    entities.j1.x -= 1
                    parametres.dernier_mouvement = temps_actuel

            # HAUT
            elif keys[pygame.K_UP]:
                if player_can_move("haut"):
                    entities.j1.y -= 1
                    parametres.dernier_mouvement = temps_actuel

            # BAS
            elif keys[pygame.K_DOWN]:
                if player_can_move("bas"):
                    entities.j1.y += 1
                    parametres.dernier_mouvement = temps_actuel


    if etat_du_jeu == 'parametre':
        UI.parametre(screen)

    if etat_du_jeu == 'rules':
        UI.rules(screen)

    if etat_du_jeu == 'combat':
        UI.combat(screen)

        if entities.ennemi_en_combat.life <= 0 :#mort de l'enemi
            grille_jeu[entities.ennemi_en_combat.x, entities.ennemi_en_combat.y].contenu = None
            entities.ennemi_en_combat = None
            etat_du_jeu = 'play'
        
        if parametres.tour_de == 'enemi':
            temps_actuel = pygame.time.get_ticks()

            if temps_actuel - parametres.dernier_changement > parametres.delai_combat:
            
                if entities.ennemi_en_combat.life<=10 :
                    entities.ennemi_en_combat.se_soigner()
                    parametres.tour_de = 'Joueur'

                if entities.ennemi_en_combat.life>=10 :
                    entities.ennemi_en_combat.attaquer(entities.j1)
                    parametres.tour_de = 'Joueur'
        
    pygame.display.flip()

pygame.quit()

#lalallalalalala
