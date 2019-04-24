#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

Cantidad = float(input('Cantidad a invertir:'))
Interés = float (input('Tipo de interés:'))
Años = float (input('cantidad de años:'))
print ('Capital final: ' + str (round(Cantidad * (Interés / 100+1) ** Años , 2)))


