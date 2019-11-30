#crea una lista 
animales=["elefante","leon","tigre","jirafa"]
print(animales)

animales[1:3]=["gato"] #reemplaza 'leon' y 'tigre' con un solo elemento: 'gato'
print(animales)

animales[1:3]=[] #remueve los dos elementos 'gato' y 'jirafa'
print(animales)

animales=animales.clear
print(animales)