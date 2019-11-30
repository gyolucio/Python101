#Para utilizar una función de un módulo lo debemos importar

import datetime
ahora=datetime.datetime.now()
print(ahora)

print(ahora.strftime("%a-%Y-%m-%d")) #BUSCAR PARÁMETROS %a %Y %m etc. etc. para ver cómo mostrar la fecha y hora en el formato que se quiera