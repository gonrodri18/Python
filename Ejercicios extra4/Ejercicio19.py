# Escribir una función con tres argumentos enteros y devuelta el que está en la posición intermedia. 
# Utilizar esta función en un programa que pregunte al usuario tres números y le devuelva el que está en la posición intermedia (la mediana)

def medio (a,b,c):
    lista = [a,b,c]
    lista.sort()
    return (lista[1])

M=float(input("Introduce el primer numero:  "))
N=float(input("Introduce el segundo numero:  "))
P=float(input("Introduce el tercer numero:  "))
print("La mediana es", medio(M,N,P))