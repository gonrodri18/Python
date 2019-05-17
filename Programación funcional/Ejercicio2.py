# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. 
# La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

from math import  sin, cos, tan, exp, log  

def calcula ():
    funciones = {'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp, 'log': log}
    función = input ('Que función queires aplicar (sin, cos, tan, exp, log):')
    valor = int (input('Introduce un valor:'))
    for i in range (1, valor+1):
        print (i, '\t', funciones[función](i))
    return

calcula()
    
