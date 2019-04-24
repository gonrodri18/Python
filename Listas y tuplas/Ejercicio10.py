#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]
for i in precios:
    if i < min:
        min = i
    elif i > max:
        max = i
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))

