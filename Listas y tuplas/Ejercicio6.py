asignaturas = ['Mates' , 'Lengua' , 'Física']
suspenso = []
for i in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + i + "? "))
    if nota < 5:
        suspenso.append(i)
print("Tienes que repetir " + str(suspenso))


