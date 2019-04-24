#Escribir un programa que pregunte al usuario cuantos números de Fibonacci se deben generar, e imprimirlos. 
# La sucesión de Fibonnaci empieza con 1 y 1, y cada número a partir de ests dos es la suma de los dos anteriores.

n = int(input('Hasta que número quieres que imprima?:'))
x = [1,1]
for i in range (1,n+1):
    x.append(x[-1]+x[-2])
print(x)





