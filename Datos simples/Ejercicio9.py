#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la inversión redondeado con dos decimales.


c = float(input('cantidad a invertir:'))
i = float (input('interés anual:'))
y = int(input('Numero de años:'))
print ('Capital final:' + str (round (c * (i/100 + 1) ** y,2 )))

