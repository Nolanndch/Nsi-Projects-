import parametres
import random


class Player:  # classe des joueurs
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = 50
        self.max_life = 50
        self.armor = 0
        self.max_armor = 50
        self.power = 100
        self.couleur = parametres.NOIR
        self.inventaire = []
        self.nb_deplacement = 0
        self.xp = 0
        self.niveau = 0

    def attaquer(self, enemi):
        enemi.life -= self.power

    def soigner(self):
        if self.life + soin.pv <= self.max_life and soin in self.inventaire:
            self.life += soin.pv
            self.inventaire.pop()

    def proteger(self, pv):
        self.life += pv

    def se_deplacer(self, direction):
        if direction == "droite":
            self.x += 1
        elif direction == "gauche":
            self.x -= 1
        elif direction == "haut":
            self.y -= 1
        elif direction == "bas":
            self.y += 1

        self.nb_deplacement += 1

    def gain_xp(self):
        self.xp += random.randint(5, 10)
        while self.xp >= 10:
            self.xp -= 10
            self.niveau += 1


j1 = Player(5, 6)
j2 = Player(10, 5)


class Mob:  # classe des enemis
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coord = x, y
        self.life = 50
        self.max_life = 50
        self.power = 10
        self.soin_restant = 3
        self.nb_deplacement = 0
        self.couleur = parametres.ROUGE_FONCE

    def attaquer(self, player):
        if player.armor > 0:
            player.armor -= 5
        else:
            player.life -= 5

    def se_soigner(self):
        if self.soin_restant > 0:
            self.life += 5
            self.soin_restant -= 1

    def se_deplacer(self, grille):

        if j1.x > self.x and grille[self.x + 1, self.y].contenu == None:
            self.x += 1
        if j1.x < self.x and grille[self.x - 1, self.y].contenu == None:
            self.x -= 1
        if j1.y > self.y and grille[self.x, self.y + 1].contenu == None:
            self.y += 1
        if j1.y < self.y and grille[self.x, self.y - 1].contenu == None:
            self.y -= 1
        """
        else:
            if not grille[self.x + 1, self.y].contenu == None:
                self.x -= 1
            if not grille[self.x - 1, self.y].contenu == None:
                self.x += 1
            if not grille[self.x, self.y + 1].contenu == None:
                self.x += 1
            if not grille[self.x - 1, self.y].contenu == None:
                self.x += 1
        """

        self.nb_deplacement += 1


ennemi_en_combat = None


class Objet:
    def __init__(self, name, pv, degat, protection, couleur):
        self.name = name
        self.pv = pv
        self.degat = degat
        self.protection = protection
        self.couleur = couleur

    def nom_objet(self):
        return self.name

    def nb_degat(self):
        j1.power += self.nb_degat

    def regen(self):
        j1.life += self.pv

    def proteger(self):
        if parametres.tour_de_jcj == "j1":
            j1.armor += self.protection
        else:
            j2.armor += self.protection


soin = Objet("soin", 2, 0, 0, parametres.VERT_FONCE)
épée = Objet("épée", 0, 5, 0, parametres.GRIS_FONCE)
armure = Objet("plastron", 0, 0, 10, parametres.BLEU_FONCE)
