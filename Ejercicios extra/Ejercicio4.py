#Dada la lista de números  lista=[1,4,62,78,32,23,90,24,2,34]. Preguntar por un número e imprimir los números de la lista por encima de dicho nu ́mero. 

lista = [1,4,62,78,32,23,90,24,2,34]
números = int(input ('Elije un número [1,4,62,78,32,23,90,24,2,34]:'))
for i in lista:       #Sacar elemento de lista
    if i > números:   #Comparar elemento con N
        print (i)

