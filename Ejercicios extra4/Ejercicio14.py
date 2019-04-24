# Un número se dice que es perfecto si la suma de sus divisores, excluyendo el número, es igual al número. 
# Por ejemplo, 28 es perfecto porque sus divisores son 1, 2, 4, 7, 14 y 28, y tenemos 1 + 2 + 4 + 7 + 14 = 28. 
# Escribir un programa que encuentre los números perfectos entre uno y diez mil.

def sumadiv(n):
    suma = 0
    for i in range(1,n):
        if n%i == 0:
            suma += i
    return (suma)
for i in range (1, 100001 ):
    if sumadiv(i) == i:
        print (i)
    


