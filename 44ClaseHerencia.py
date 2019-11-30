class Instrumento:
    def __init__(self, precio):
        self.precio = precio

    def tocar(self):
        print ("Estamos tocando musica")

    def romper(self):
        print ("Eso lo pagas tú!\nson", self.precio, "$$$")

class Bateria(Instrumento):
    pass

class Guitarra(Instrumento):
    def __init__(self,precio,cuerdas):
        self.precio=precio
        self.cuerdas=cuerdas
        self.romper()
        super().romper()
    def romper(self):
        print("Romper en la guitarra")

otra_guitarra=Guitarra(2023,12)

G=Guitarra(9000,10)

