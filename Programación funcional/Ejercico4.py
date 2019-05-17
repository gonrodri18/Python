#Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.

def calificacion(nota):
    if nota < 5:
        return 'SS' 
    elif nota < 7:
        return 'AP'
    elif nota < 9:
        return 'NT'
    else:
        return 'SB'

def aplica_calificacion(notas):
    #return list(map(calificacion, notas))
    #Con compresión de listas:                                                 
    #Ejercicio 6:
    return {nombre:calificacion(nota) for nombre,nota in notas.items() if  nota>= 5} #Para que imprima los aprobados

print (aplica_calificacion ({'Mates':8, 'Fisica':6.5, 'Quimica':9.2, 'Economia':3.1 }))

