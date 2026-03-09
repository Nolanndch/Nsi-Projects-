import parametres

class Player():  #classe des joueurs
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = 50
        self.max_life = 50
        self.armor = 20
        self.max_armor = 20
        self.power = 10
        self.couleur = parametres.BLEU_FONCE
        self.inventaire = [1,1,1,1]


    def attaquer(self, mob):
        mob.life -= self.power

    def soigner(self,pv):
        if self.life + pv <= self.max_life and 1 in self.inventaire :
            self.life += pv
            self.inventaire.remove(1)
    
    def proteger(self,pv):
        self.life += pv
        

j1 = Player(5, 6)

class Mob():   #classe des enemis
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = 50
        self.max_life = 50
        self.power = 10
        self.soin_restant = 1
        self.couleur = parametres.ROUGE_FONCE
    
    def attaquer(self, player):
        if player.armor > 0 :
            player.armor-=5
        else :
            player.life-=5

    def se_soigner(self):
        if self.soin_restant > 0 :
            self.life += 5 
            self.soin_restant-=1

ennemi_en_combat = None
