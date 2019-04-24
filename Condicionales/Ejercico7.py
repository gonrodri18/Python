#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.


Peso=input('¿Cuánto pesas?:')
Estatura=input('¿Cuánto mides?:')
imc = round(float(Peso)/float(Estatura)**2,2)
print('Tu índice de masa corporal es ' + str(imc))
