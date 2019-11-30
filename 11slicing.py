#str[inicio:fin] ## 1. toma del inicio hasta el fin -1
#str[inicio:] ## 2. toma del inicio hasta el resto del arreglo
#str[:fin] ## 3. toma del inicio hasta el fin -1
#str[:] ## 4. toma todo el arreglo
"Hola"[:] #Imprime 'Hola0' (Todo el arreglo)
"Hola"[0:] #Imprime 'Hola' (el primer caracter y el resto del arreglo)
"Hola"[1:3] #Imprime 'ol' (el segundo y tercer caracter)
"Hola"[:3] #Imprime 'Hol' (los primeros tres caracteres)

monty_python="Monty Python"
monty=monty_python[:5]
print(monty)
python=monty_python[-6:] #o con slicing sería python=monty_python[6:]
print(python)