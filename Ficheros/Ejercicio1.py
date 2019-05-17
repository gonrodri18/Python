#Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

n = int(input('Dame un número:'))
archivo = 'tabla -' + str(n) + '.txt'
f = open (archivo, 'w')
for i in range (1, 11):
    f.write (str (n) + '*' + str(i) + '=' + str (n * i) + '\n')
f.close ()



