#Método append() para agregar un elemnto a una lista
#Ej es posible cambiar el contenido de una lista usando
lista=[1,2,3,4,5,6,7,8,9,10]
print(lista)
#lista[index]=nuevo_elemento
lista[4]=100
print(lista)

#crea una lista 
animales=["elefante","leon","tigre","jirafa"]
print(animales)

#agrega dos elementos a la lista
animales+=["chimpancé","lobo"]
print(animales)

#agrega un elemento a la lista utilizando append()
animales.append("rinoceronte")
print(animales)

#reemplazar 'rinoceronte' con 'dinosaurio'
rino=int(len(animales))-1
print(rino)
animales[rino]="dinosaurio" #reemplaza 'rinoceronte' por 'dinosaurio
print(animales)
animales.remove("dinosaurio") #remueve el objeto especificado de la lista
print(animales)

nombres=["pepe", "juan"]
animales.extend(nombres)
print(animales)
