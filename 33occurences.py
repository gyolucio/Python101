frankenstein=open("Frankenstein.txt","r",encoding='utf-8')
archivo=frankenstein.read()
contador_dict={}

def limpia_puntuacion(palabra,puntuacion):
    palabra_limpia=""
    if puntuacion in palabra:
        for letra in palabra:
            if not letra == puntuacion:
                palabra_limpia+=letra
    else:
        palabra_limpia = palabra
    return palabra_limpia

def limpia_palabra(palabra):
    palabra=palabra.strip() #para remover espacios
    palabra=limpia_puntuacion(palabra,",")
    palabra=limpia_puntuacion(palabra,".")
    palabra=limpia_puntuacion(palabra,":")
    palabra=limpia_puntuacion(palabra,"?")
    palabra=limpia_puntuacion(palabra,"!")
    palabra=limpia_puntuacion(palabra,"'")
    palabra=limpia_puntuacion(palabra,"\"")
    palabra=limpia_puntuacion(palabra,")")
    palabra=limpia_puntuacion(palabra,"()")
    palabra=limpia_puntuacion(palabra,"]")
    palabra=limpia_puntuacion(palabra,"[")
    return palabra

for linea in archivo:
    palabras=linea.split(" ")
    for palabra in palabras:
        palabra=limpia_palabra(palabra)
        if palabra in contador_dict.keys() and palabra !="":
            contador_dict[palabra]+=1
        else:
            contador_dict[palabra]=1

contador_dict=[(k, contador_dict[k]) for k in sorted(contador_dict, key=contador_dict.get, reverse=True)]

for key, value in contador_dict:
    print(key + " = " + str(value))

print("Palabras únicas encontradas: " + str(len(contador_dict)))