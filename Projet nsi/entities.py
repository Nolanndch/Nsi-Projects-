import parametres

class Player():  #classe des joueurs
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = 50
        self.power = 10
        self.couleur = parametres.BLEU_FONCE

    def attaquer(self, mob):
        mob.life -= self.power

    def soigner(self,pv):
        self.life += pv
    
    def proteger(self,pv):
        self.life += pv

j1 = Player(5, 6)

class Mob():   #classe des enemis
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = 50
        self.power = 30
        self.couleur = parametres.ROUGE_FONCE
    
    def attaquer(self, player):
        player.life -= self.power

    def se_soigner(self):
        self.life+=5

ennemi_en_combat = None

'''''
Pas encore finie
class Objet():
    def __init__(self,name, pv, degat, protection):
        self.name = name
        self.pv = pv
        self.degat = degat
        self.protection = protection
    
    def nom_objet(self):
        return self.name
    
    def nb_degat(self):
        Player.power += self.nb_degat 

    def pv(self):
        Player.life += self.pv
    
    def protection(self):
        Player.life += 
'''
