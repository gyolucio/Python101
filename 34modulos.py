#Podemos generar nuestros propios modulos
#CREA UN ARCHIVO LLAMADO mi_modulo.py Y ESCRIBE ESTE CODICO
#""" Documentación para el módulo mi_modulo
#Este modulo contiene la función hola_mundo
#"""
#def hola_mundo(name):
#    print("Hello, World! My name is %s" % name)

####
#Para utilizar una función de un módulo lo debemos importar.
#import mi_modulo

import mi_modulo
mi_modulo.hola_mundo("PEPE EL TORO")