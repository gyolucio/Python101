class Coche(object):
    """Abstraccion de los objetos coche."""
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("Tenemos " + str(gasolina) + " litros")

    def arrancar(self):
        if self.gasolina > 0:
            print ("Arranca coche!")
        else:
            print ("No arranca...")

    def conducir(self):
        if self.gasolina > 0:
            print ("Quedan" , self.gasolina , "litros") #AQUÍ NO PIDE CONVERTIR str(self.gasolina) porque se concatenó con comas ',' y no con
            self.gasolina -= 1                          #el operador '+'
        else:
            print ("No se mueve...")

gas=10
Camaro=Coche(gas)
for i in range(gas+1):
    Camaro.conducir()