#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Introduce una palabra: ")
vocales= ['a', 'e', 'i', 'o', 'u']
for m in vocales: 
    times = 0
    for j in palabra: 
        if j == m :
            times += 1
    print("La vocal " + m + " aparece " + str(times) + " veces")

