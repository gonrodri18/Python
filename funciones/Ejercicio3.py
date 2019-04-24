#Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factura(n):
    """Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp

print(factura(4))
print(factura(20))