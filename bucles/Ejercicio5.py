# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

c = float(input ('cantidad a invertir:'))
I = float(input ('Interés anual:'))
N = int (input('Número de años:'))
for i in range (N):
    c *= 1 + I/100
    print ( 'Capital tras ' + str(i+1) + 'años: '  + str(round(c, 2)))


