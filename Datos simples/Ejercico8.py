#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n1 = input('Número entero 1:')
n2 = input ('Número entero 2:')
print (n1 + ' entre ' + n2 + ' da un cociente' + str(int(n1)// int(n2)) + 'y un resto' + str (int (n1) % int(n2)))