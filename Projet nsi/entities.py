import parametres

class Player():  #classe des joueurs
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = 50
        self.max_life = 50
        self.armor = 20
        self.max_armor = 20
        self.power = 100
        self.couleur = parametres.BLEU_FONCE
        self.inventaire = [1,1,1,1]
        self.nb_deplacement = 0


    def attaquer(self, mob):
        mob.life -= self.power

    def soigner(self,pv):
        if self.life + pv <= self.max_life and 1 in self.inventaire :
            self.life += pv
            self.inventaire.remove(1)
    
    def proteger(self,pv):
        self.life += pv
    
    def se_deplacer(self,direction):
        if direction == 'droite':
            self.x+=1
        elif direction == 'gauche':
            self.x-=1
        elif direction == 'haut':
            self.y-=1
        elif direction == 'bas':
            self.y+=1

        self.nb_deplacement+=1
        

j1 = Player(5, 6)

class Mob():   #classe des enemis
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.coord = x,y
        self.life = 50
        self.max_life = 50
        self.power = 10
        self.soin_restant = 3
        self.nb_deplacement = 0
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

    def se_deplacer(self):

        if j1.x > self.x :
            self.x+=1
        if j1.x < self.x :
            self.x-= 1
        if j1.y > self.y :
            self.y+=1
        if j1.y < self.y :
            self.y-= 1

        self.nb_deplacement+=1
        print("mob",self.x,self.y)
            

ennemi_en_combat = None

class Objet():
    def __init__(self,name, pv, degat, protection):
        self.name = name
        self.pv = pv
        self.degat = degat
        self.protection = protection
        self.couleur = parametres.VERT_FONCE
    
    def nom_objet(self):
        return self.name
    
    def nb_degat(self):
        j1.power += self.nb_degat 

    def pv(self):
        j1.life += self.pv
    
    def protection(self):
        j1.armor += self.protection
        
soin = Objet("soin", 10, 0, 0)
épée = Objet("épée", 0, 5, 0)
armure = Objet("plastron", 0, 0, 5)   

