import random

class Dado(object):
  def tirar(self):
    print("El dado arroja: " +str(random.randint(1,6)))

JUEGO=Dado()

for i in range(3):
    JUEGO.tirar()

##############################
####DADO DE MÁS DE 6 CARAS####
##############################
import random

class Dado():
    def __int__(self,lados):
        self.lados=lados
    def tirar(self):
        return random.randint(1,lados)

dado_6_lados=Dado(6)
dado_12_lados=Dado(12)
dado_24_lados=Dado(24)

print(dado_6_lados.tirar())
print(dado_12_lados.tirar())
print(dado_24_lados.tirar())
