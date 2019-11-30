#Crear un diccionario donde se lea todo el archivo y cree una nueva variable cada vez que se encuentre una palabra nueva, si la 
#palabra no es nueva, entonces que cuente cuántas veces se ha repetido esa palabra

#TIP PARA CONTADOR
#d={}
#d["Hola"]=1
#d
#d["Dios"]=1
#d
#d["Dios"]+=1
#d

frankenstein=open("Frankenstein.txt","r",encoding='utf-8')
text=frankenstein.read()
diccionario={}
for palabra in text:
    contador=diccionario.get(palabra,0)
    diccionario[palabra]=contador+1

diccionario_lista=diccionario.keys()

for palabras in diccionario_lista:
    print (palabras,diccionario[palabras])
frankenstein.close


# texto_minusculas=text.read().lower()  #PARA CONVERTIR EN MINUSCULAS
#contador=0
#for lines in text:




#a=0
#for linea in frankenstein: 
 #  a+=1
#frankenstein.close

#renglon={}
#contador=0
#for linea in frankenstein: 
 #   while True
  #  if "\n" in frankenstein
    
#frankenstein.close

#print(palabra)
