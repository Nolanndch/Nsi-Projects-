import parametres

class player():
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

j1 = player(5, 6)

class mob():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = 20
        self.power = 5
        self.couleur = parametres.ROUGE_FONCE
    
    def attaquer(self, player):
        player.life -= self.power

ennemi_en_combat = None
