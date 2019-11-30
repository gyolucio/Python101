class Persona(object):
  def __init__(self, name):  #__init__ FUNCIÓN DE INICIALIZACIÓN, DONDE SE INTRODUCEN LOS OBJETOS DONDE QUE SERÁN NECESARIOS PARA CORRER EL PROGRAMA
    self.name = name
  
  def saluda(self):
    print("Hola " + self.name)

  def despidete(self):
    print("Adios " + self.name)

p=Persona("Ana")
p.saluda()
p.despidete()

c=Persona("Jessica")
c.saluda()
c.despidete()