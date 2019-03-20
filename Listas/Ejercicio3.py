asignaturas = ['Mates' , 'Lengua' , 'Física']
notas = []
for i in asignaturas:
    notas.append (input ('¿Qué has sacado en ' + i + '? '))
for i in range(len(notas)):
    print ( 'En ' + asignaturas [i] + ' has sacado un ' + notas[i])