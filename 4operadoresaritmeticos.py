#divide el valor almacenado en la variable numero entre 2 y vamos a calcular el residuo
numero=9.0 #variable flotante
resultado=numero/2 #operador '/' de división
residuo=numero%2 #operador '%' de módulo
#El operador módulo no hace otra cosa que devolver el resto de la división entre los dos operandos. 
# #En el ejemplo, 9 / 2 sería 4, con 1 de residuo, luego el módulo es 1.
print("resultado="+str(resultado))
print("residuo="+str(residuo))

#ORDEN DE PRECEDENCIA
# Exponente: **
# Multiplicación, División, División entera, Módulo: *, /, //, %
# Suma, Resta: +, -