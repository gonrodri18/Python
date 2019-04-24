#Escribir un programa que tenga como variables dos números, y como retorno el máximo de los dos, sin utilizar la función max() de Python.
#Utilizar esta función para escribir una función que calcule el máximo de tres números. 
#Generalizarlo para cualquier número de variables. “retorne” el mayor de los tres, sin utilizar la función.

def mama(n,z):
    if n > z:
        return (n)
    else:
        return(z)

def max(a, *b):
    m = a
    for i in b:
        m = mama(m,i)
    return m
print(max(2,3,4,5,8))

   
    


