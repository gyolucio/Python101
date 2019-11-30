#Generaremos un archivo CSV de una lista de personas:


archivo=open("datos.txt","w")
while True:
    persona=input("Nombre de la persona: ")
    if persona=="salir":
        print("Adios")
        break
    else:
        datos=input("Datos de "+persona+": ")
        archivo.write(persona+", "+datos+"\n")
archivo.close()