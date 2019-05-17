# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. 
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello

n = int(input('Escriba un número netero:'))
m = int(input('Escriba otro número entero:'))
archivo = 'tabla -' + str(n) + '.txt'
fd = open(archivo, 'r')
Gonzalo = fd.readlines()
print (Gonzalo[m-1])


