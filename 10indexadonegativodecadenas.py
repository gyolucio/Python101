#Es posible utilizar indexado negativo que parte desde el último caracter de una cadena
#Utilizando el indexado negativo, obtener el signo '!' de la cadena de mensaje 'Tenga cuidado al subir la escalera!'
mensaje="Tenga cuidado al subir la escalera!"
exclamacion=mensaje[-1] #Se empieza desde el -1 para obtener el último caracter (-2 para obtener el penúltimo, -3 para obtener el antepenúltimo, etc.)
print(exclamacion)