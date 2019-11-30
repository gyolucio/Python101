import random
class Player(object):
    def __init__(self,name):
        self.name=name
        self.health=random.randint(90,200)
        self.level=1
    def powerup(self):
        morehealth=random.randint(89,130)
        self.health += morehealth
        self.level+=1
        print("Has subido a nivel",self.level,"! ahora tienes",self.health,"puntos de vida!")
    def takedamage(self):
        daño=random.randint(55,100)
        self.health -= daño
        if self.health > 0:
            print("Has recibido",daño,"puntos de daño! tu vida restante es",self.health)
        else:
            print("Has recibido un ataque crítico de",daño,"puntos de daño que ha acabado con tu vida!\nRestart?")
    def showHealth(self):
        print("\nHola",self.name,"eres nivel",self.level,"y tienes",self.health,"puntos de vida")

player1=Player("DOOMGUY")
player1.showHealth()
player1.takedamage()
player1.powerup()
player1.takedamage()
player1.powerup()
player1.showHealth()


player2=Player("LINK")
player2.showHealth()
player2.takedamage()
player2.takedamage()
player2.powerup()
player2.showHealth()
