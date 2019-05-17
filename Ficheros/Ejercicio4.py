# Leer tabla -n.txt e imprimr número de palabras.

n = int(input('Escribe un número:'))
f = open ('tabla -' + str(n) + '.txt', 'r')
leer = f.read()
print(len(leer.split()))

