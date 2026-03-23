import pygame
import parametres
import bouton
import UI
import fonction
import entities
from fonction import player_can_move

screen = parametres.ecran
grille_jeu = fonction.creer_grille(parametres.taille_grille)
grille_1c1 = fonction.creer_grille(parametres.taille_grille)
fonction.contenue_grille(grille_jeu, 1)
fonction.contenue_grille(grille_1c1, 2)
fonction.tour()

clock = pygame.time.Clock()

loop = True
while loop:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:  # les verifs des click clavier

            if event.key == pygame.K_ESCAPE:
                fonction.etat_precedent(loop)

            if event.key == pygame.K_e:
                loop = False

            if event.key == pygame.K_a:
                parametres.etat_du_jeu = "niveau"

        if event.type == pygame.MOUSEBUTTONDOWN:  # les verifs des boutons

            if bouton.exit_bt.collidepoint(pygame.mouse.get_pos()):
                fonction.etat_precedent(loop)

            if parametres.etat_du_jeu == "menu":
                if bouton.Jouer_bt.collidepoint(pygame.mouse.get_pos()):
                    parametres.etat_du_jeu = "play"
                if bouton.parametre_bt.collidepoint(pygame.mouse.get_pos()):
                    parametres.etat_du_jeu = "parametre"
                if bouton.rules_bt.collidepoint(pygame.mouse.get_pos()):
                    parametres.etat_du_jeu = "rules"
                if bouton.jcj_bt.collidepoint(pygame.mouse.get_pos()):
                    parametres.etat_du_jeu = "jcj"

            if parametres.etat_du_jeu == "parametre":

                # gestion des click de selection de la difficulté

                if bouton.facile_bt.collidepoint(pygame.mouse.get_pos()):
                    fonction.change_dificulty("facile", grille_jeu)

                if bouton.moyen_bt.collidepoint(pygame.mouse.get_pos()):
                    fonction.change_dificulty("moyen", grille_jeu)

                if bouton.difficile_bt.collidepoint(pygame.mouse.get_pos()):
                    fonction.change_dificulty("difficile", grille_jeu)

            if parametres.etat_du_jeu == "combat":  # deroulement du combat coté joueur

                if (
                    entities.ennemi_en_combat != None and parametres.tour_de == "Joueur"
                ):  # verfifie le tour du joueur

                    if bouton.attaquer_bt.collidepoint(pygame.mouse.get_pos()):
                        entities.j1.attaquer(entities.ennemi_en_combat)
                        parametres.tour_de = "enemi"
                        parametres.dernier_changement = pygame.time.get_ticks()

                    if bouton.soin_bt.collidepoint(pygame.mouse.get_pos()):
                        entities.j1.soigner(5)

            if parametres.etat_du_jeu == "niveau":  # selection de l'amelioration

                if bouton.more_deplacement_bt.collidepoint(pygame.mouse.get_pos()):
                    parametres.deplacement_joueur_max += 1
                    fonction.etat_precedent(loop)

                if bouton.more_life_bt.collidepoint(pygame.mouse.get_pos()):
                    entities.j1.max_life += 10
                    entities.j1.life += 10
                    fonction.etat_precedent(loop)

                if bouton.more_force_bt.collidepoint(pygame.mouse.get_pos()):
                    entities.j1.power += 10
                    fonction.etat_precedent(loop)

            if parametres.etat_du_jeu == "combat_jcj":  # deroulement du combat en jcj

                if parametres.tour_de_jcj == "j1":  # verfifie le tour du joueur

                    if bouton.attaquer_bt.collidepoint(pygame.mouse.get_pos()):
                        temps_actuel = pygame.time.get_ticks()
                        if (
                            temps_actuel - parametres.dernier_changement
                            > parametres.delai_combat
                        ):
                            entities.j1.attaquer(entities.j2)
                            parametres.tour_de_jcj = "j2"
                            parametres.dernier_changement = temps_actuel
                            # mort du joueur
                            if entities.j2.life <= 1:
                                parametres.etat_du_jeu = "mort"

                if parametres.tour_de_jcj == "j2":  # verfifie le tour du joueur

                    if bouton.attaquer_bt.collidepoint(pygame.mouse.get_pos()):
                        temps_actuel = pygame.time.get_ticks()
                        if (
                            temps_actuel - parametres.dernier_changement
                            > parametres.delai_combat
                        ):
                            entities.j2.attaquer(entities.j1)
                            parametres.tour_de_jcj = "j1"
                            parametres.dernier_changement = temps_actuel
                            # mort du joueur
                            if entities.j1.life <= 1:
                                parametres.etat_du_jeu = "mort"

    if parametres.etat_du_jeu == "menu":
        UI.menu(screen)

    if parametres.etat_du_jeu == "play":
        UI.play(screen, grille_jeu, entities.j1)

        clock.tick(60)  # limite à 60 FPS

        temps_actuel = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        if parametres.tour_deplacement == "mob":  # déplacements des mobs

            fonction.bouger_mob(grille_jeu)
            fonction.player_rencontre(grille_jeu)

        if parametres.tour_deplacement == "joueur":

            if (
                temps_actuel - parametres.dernier_mouvement > parametres.delai_mouvement
            ):  # delai mouvement du joueur

                if entities.j1.nb_deplacement <= parametres.deplacement_joueur_max:

                    # DROITE
                    if keys[pygame.K_RIGHT]:
                        if player_can_move("droite"):
                            entities.j1.se_deplacer("droite")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_jeu)

                    # GAUCHE
                    elif keys[pygame.K_LEFT]:
                        if player_can_move("gauche"):
                            entities.j1.se_deplacer("gauche")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_jeu)

                    # HAUT
                    elif keys[pygame.K_UP]:
                        if player_can_move("haut"):
                            entities.j1.se_deplacer("haut")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_jeu)

                    # BAS
                    elif keys[pygame.K_DOWN]:
                        if player_can_move("bas"):
                            entities.j1.se_deplacer("bas")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_jeu)
                else:
                    parametres.tour_deplacement = "mob"
                    entities.j1.nb_deplacement = 0

    if parametres.etat_du_jeu == "parametre":
        UI.parametre(screen)

    if parametres.etat_du_jeu == "rules":
        UI.rules(screen)

    if parametres.etat_du_jeu == "combat":
        UI.combat(screen)

        # déroulement du combat coté enemi

        if entities.ennemi_en_combat.life <= 0:  # mort de l'enemi
            niveau1 = entities.j1.niveau
            fonction.refill(grille_jeu)
            fonction.recompense(grille_jeu)
            grille_jeu[
                entities.ennemi_en_combat.x, entities.ennemi_en_combat.y
            ].contenu = None
            entities.ennemi_en_combat = None
            parametres.tour_deplacement = "joueur"
            entities.j1.gain_xp()
            niveau2 = entities.j1.niveau
            if (
                niveau1 < niveau2
            ):  # ouvre la page de selection de l'amelioration du gain de niveau
                parametres.etat_du_jeu = "niveau"
            else:
                parametres.etat_du_jeu = "play"

        if parametres.tour_de == "enemi":
            temps_actuel = pygame.time.get_ticks()

            if temps_actuel - parametres.dernier_changement > parametres.delai_combat:

                if entities.ennemi_en_combat.life <= 10:  # l'enemi se soigne si life<10
                    entities.ennemi_en_combat.se_soigner()

                # l'enemi attaque
                entities.ennemi_en_combat.attaquer(entities.j1)
                parametres.tour_de = "Joueur"

                # mort du joueur
                if entities.j1.life <= 1:
                    parametres.etat_du_jeu = "mort"

    if parametres.etat_du_jeu == "mort":
        UI.mort(screen)
        fonction.reset_grille(grille_jeu)

    if parametres.etat_du_jeu == "niveau":
        UI.niveau(screen)

    if parametres.etat_du_jeu == "jcj":
        UI.jcj(screen, grille_1c1, entities.j1, entities.j2)

        clock.tick(60)  # limite à 60 FPS

        temps_actuel = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        if parametres.tour_de_jcj == "j1":  # si c'est le tour du joueur1

            if (
                temps_actuel - parametres.dernier_mouvement > parametres.delai_mouvement
            ):  # delai mouvement du joueur

                if entities.j1.nb_deplacement <= parametres.deplacement_joueur_max:

                    # DROITE
                    if keys[pygame.K_RIGHT]:
                        if player_can_move("droite"):
                            entities.j1.se_deplacer("droite")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_1c1)

                    # GAUCHE
                    elif keys[pygame.K_LEFT]:
                        if player_can_move("gauche"):
                            entities.j1.se_deplacer("gauche")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_1c1)

                    # HAUT
                    elif keys[pygame.K_UP]:
                        if player_can_move("haut"):
                            entities.j1.se_deplacer("haut")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_1c1)

                    # BAS
                    elif keys[pygame.K_DOWN]:
                        if player_can_move("bas"):
                            entities.j1.se_deplacer("bas")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_1c1)
                else:
                    parametres.tour_de_jcj = "j2"
                    entities.j1.nb_deplacement = 0

        elif parametres.tour_de_jcj == "j2":  # si c'est le tour du joueur2

            if (
                temps_actuel - parametres.dernier_mouvement > parametres.delai_mouvement
            ):  # delai mouvement du joueur

                if entities.j2.nb_deplacement <= parametres.deplacement_joueur_max:

                    # DROITE
                    if keys[pygame.K_RIGHT]:
                        if player_can_move("droite"):
                            entities.j2.se_deplacer("droite")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_1c1)

                    # GAUCHE
                    elif keys[pygame.K_LEFT]:
                        if player_can_move("gauche"):
                            entities.j2.se_deplacer("gauche")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_1c1)

                    # HAUT
                    elif keys[pygame.K_UP]:
                        if player_can_move("haut"):
                            entities.j2.se_deplacer("haut")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_1c1)

                    # BAS
                    elif keys[pygame.K_DOWN]:
                        if player_can_move("bas"):
                            entities.j2.se_deplacer("bas")
                            parametres.dernier_mouvement = temps_actuel
                            fonction.player_rencontre(grille_1c1)
                else:
                    parametres.tour_de_jcj = "j1"
                    entities.j2.nb_deplacement = 0

    if parametres.etat_du_jeu == "combat_jcj":
        UI.combat_jcj(screen)

    pygame.display.flip()

pygame.quit()
