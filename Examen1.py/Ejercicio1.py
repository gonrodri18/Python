#Escribir un programa que realice la devolución de una cantidad dada por el usuario en monedas.
#El programa debe cumplir los siguientes requisitos:
#Solo se disponen de tres tipos de monedas: 5, 2 y 1 €. Crear una lista que contenga estos tres tipos de moneda y usar la lista en la solución.
#El programa debe preguntar al usuario por una cantidad entera de euros.
#El programa debe mostrar por pantalla el mínimo número de monedas necesarias para sumar la cantidad introducida por el usuario y cuántas monedas de cada tipo se necesitan para ello. El número de monedas de cada tipo debe guardarse en otra lista.

monedas = [5, 2, 1]
cantidad = int(input('Introduce una cantidad de euros:'))
cambio = [0, 0, 0]
for i in range (len(monedas)):
    while cantidad >= monedas [i]:                          # monedas [i], porque emezará en orden, primero 5, luego 2 y por último 1
        cantidad -= monedas[i]
        cambio [i] += 1
print ('El número mínimo de monedas es ', sum(cambio))
for i in range (len(monedas)):                              # Para que la salida sea más bonita
    print (cambio [i], ' monedas de ', monedas [i], '€')