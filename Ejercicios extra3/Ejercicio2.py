#Preguntar un número e imprimir sus divisiones

n1 = int(input ('Dime un número:'))
for i in range (1, n1+1):
    if n1%i == 0:
        print(i)
    else:
        print ('No es divisor')

