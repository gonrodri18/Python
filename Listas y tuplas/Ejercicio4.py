# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

ganadores = []
for i in range (6):
    ganadores.append (int(input ('Número ganador:')))
ganadores.sort()
print ('Los números ganadores son:' , ganadores)




