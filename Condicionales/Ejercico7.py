Peso=input('¿Cuánto pesas?:')
Estatura=input('¿Cuánto mides?:')
imc = round(float(Peso)/float(Estatura)**2,2)
print('Tu índice de masa corporal es ' + str(imc))
