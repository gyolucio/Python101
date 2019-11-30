#Imprimir paises que empiezan con M:

archivo=open("paises.txt","r")
paises=[]

for linea in archivo:
    paises.append(linea)
archivo.close()

print(paises)
print(len(paises))

for pais in paises:
    if pais[0]=="M":
        print(pais)