peso = input('tu peso corporal:')
altura = input ( 'Tu altura:')
imc = round(float(peso)/float(altura)**2,2)
print ('Tu peso corporal es ' + str(imc))