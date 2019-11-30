import random
class Baraja():
    def __init__(self):
        trajes=["♤", "♡", "♧", "♢"]
        rangos=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
#Baraja de 52 cartas disponibles

        self.barajas=[]
        #Ciclo for para cada traje en trajes
        for traje in trajes:
            #ciclo for para cada rango en rangos
            for rango in rangos:
                #concatena el rango y el traje y appen a self.barajas()
                self.barajas.append(rango+" de "+traje)

    def barajear(self):
        random.shuffle(self.barajas)
        print(self.barajas)
    
    def repartir(self):
        print(self.barajas.pop())

mi_baraja=Baraja()
mi_baraja.barajear()
mi_baraja.repartir()
mi_baraja.repartir()
mi_baraja.repartir()
mi_baraja.repartir()