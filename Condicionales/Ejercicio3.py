#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

a=int(input('Escribe un número:'))
b=int(input('Escribe otro número:'))
if b == 0:
    print('NO SE PUEDE DIVIDIR POR 0')
else:
    print(a/b)



