import random
baraja=[]
class Baraja(object):
  def __init__(self):
    trajes=["♤", "♡", "♧", "♢"]
    rangos=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for t in trajes:
      for r in rangos:
        carta="{} de {}".format(r,t)
        baraja.append(carta)
        #print("t=",t)
        #print("r=",r)
    print(baraja)
    #print(len(baraja))
  
  def barajear(self):
    for i in range(7):  #Barajea 7 veces
      random.shuffle(baraja) #Reasigna la lista aleatoriamente 
      i
    print(baraja)

  def repartir(self):
    carta=random.choice(baraja)
    print(carta)

    # sacar una carta aleatoria de la lista de cartas 

mi_baraja = Baraja()
mi_baraja.barajear()
mi_baraja.repartir()

#Esto para probar los cambios de git
#CAMBIOS