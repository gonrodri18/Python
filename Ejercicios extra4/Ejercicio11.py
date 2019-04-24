# Como hemos visto en clase de aritm ́etica modular, los nu ́meros en base 2 solamente utilizan 0 y 1 en su representación. 
# Un número en base 2 se convierte a base 10 multiplicando por las correspondientes potencias de 2. 
# Por ejemplo, para convertir 101101 empezamos a leerlo desde la derecha y multiplicamos por las correspondientes potencias:
# 101101base2=1×20 +0×21 +1×22 +1×23 +0×24 +1×25 = = 1 + 4 + 8 + 32 = 45
# Escribir un programa que lea un nu ́mero en base 2 como una cadena, cuya longitud no sabemos de antemano, y lo convierta en un int en base 10

n = int(input('Escriba un número positivo en base 2:'))
resultado = 0
z = 1

while n != 0:
    resto = n%10
    n// = 10
    potencia = resto*z
    resultado = resto*potencia
    w.append (n)
print (n)
    

 

