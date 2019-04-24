#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por pantalla su producto escalar.

V1 = [1,2,3]
V2 = [-1,0,2]
product = 0
for i in range(len(V1)):
    product += V1[i] * V2[i]
print("El producto de los vectores" + str(V1) + " y " + str(V2) + " es " + str(product))