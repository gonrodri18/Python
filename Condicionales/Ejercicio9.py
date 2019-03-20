Cantidad = float(input('Cantidad a invertir:'))
Interés = float (input('Tipo de interés:'))
Años = float (input('cantidad de años:'))
print ('Capital final: ' + str (round(Cantidad * (Interés / 100+1) ** Años , 2)))


