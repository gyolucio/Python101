#Podemos importar el contenido de un archivo usando open, el cual recibe dos parámetros, el nombre del archivo con la ruta y el modo, 'r' para
#lectura y 'w' para escritura

#Lista de países: https://paste.ee/p/0EvRF
#Guardar en un archivo llamado paises.txt

archivo=open("paises.txt","r")

for linea in archivo: 
    print(linea.strip())
archivo.close
