curso = {'Matemáticas' : 6, 'Física': 4, 'Química' : 5}
suma = 0
for asignaturas, creditos in curso.items():
    print (asignaturas, 'tiene', creditos, 'créditos')
    suma += creditos
print ('El curso tiene', suma, 'créditos')

