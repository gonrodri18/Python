c = float(input('cantidad a invertir:'))
i = float (input('interés anual:'))
y = int(input('Numero de años:'))
print ('Capital final:' + str (round (c * (i/100 + 1) ** y,2 )))

#no entiendo