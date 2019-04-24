#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo

def mcd (n, m):
    """
    Función que calcula el máximo común divisor de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """
    resto = 1
    while resto != 0:
        resto = n % m
         n = m
         m = resto
    return n

mcd(36, 24)
