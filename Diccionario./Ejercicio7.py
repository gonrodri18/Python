cesta = {}
continuar = True
suma = 0
while continuar:
    producto= input( '¿Qué producto queires comparar?' )
    valor = float(input ('Introduce el precio de ' + producto + ': '))  #si pones float, puedes poner decimales.                                                                   
    cesta[producto] = valor                                             #si pones int, solo puedes poner números sin decimales.
    suma += valor
    respuesta = input ('¿Quieres continuar (S/N)?')
    if respuesta == 'N':
        continuar = False
for producto, valor in cesta.items():
    print (producto, valor)
print ('Total ', '\t', suma)