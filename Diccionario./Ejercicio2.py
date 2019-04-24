#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>

usuario = {}
usuario ['nombre'] = input ('Introduce tiu nombre:') #asocias la cadena de input a la clave nombre
usuario ['edad'] = input ('Introduce tu edad:')
usuario ['direccion'] = input ('Introduce tu dirección:')
print (usuario.get ('nombre'), 'tiene ', usuario.get ('edad'), 'vive en', usuario.get('direccion'))
