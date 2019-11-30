#Un diccionario es similar a una lista, con la excepción de que tú accede a su valor 
# con una llave en lugar de con un indice. Una llave puede ser una cadena o un numero

#Los diccionarios están definidos con llaves
#Ejemplo dct={'key1':"value1",'key2':"value2"}

diccionario_elaboracion={'elaboracion':'sustantivo derivado del verbo elaborar'}

#crea un diccionario telefonico

phonebook={"John":123,"Jane":234,"Gerard":345} #John, Jane y Gerard son llaves y los numeros son sus valores
print(phonebook)

#añade un nuevo item al phonebook

phonebook["Jill"]=456
print(phonebook)

#Remueve una llave-valor del phonebook
del phonebook["John"]
print(phonebook)

#Imprime el número telefónico de Jane
print(phonebook["Jane"])
print(phonebook.keys())
print(phonebook.values())

