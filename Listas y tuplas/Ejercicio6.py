# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir

asignaturas = ['Mates' , 'Lengua' , 'Física']
suspenso = []
for i in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + i + "? "))
    if nota < 5:
        suspenso.append(i)
print("Tienes que repetir " + str(suspenso))


