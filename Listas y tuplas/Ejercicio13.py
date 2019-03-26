#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una tupla y muestre por pantalla su media y desviación típica.

numeros = input ('introduce un muestra de númros separada por comas:')
numeros = numeros.split(',')
n = len(numeros)
for i in range(n):
    numeros[i] = int(numeros[i])
numeros = tuple(numeros)
sum = 0
sumsq = 0
for i in numeros:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)


