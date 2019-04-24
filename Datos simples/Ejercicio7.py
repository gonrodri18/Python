#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.


peso = input('tu peso corporal:')
altura = input ( 'Tu altura:')
imc = round(float(peso)/float(altura)**2,2)
print ('Tu peso corporal es ' + str(imc))