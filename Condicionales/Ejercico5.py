nombre = input("¿Cómo te llamas? ")
sexo = input("¿Cuál es tu sexo? ")
if (nombre <= 'M' and sexo== 'mujer') or (nombre >= 'N' and sexo== 'hombre'):
    print ('Grupo A')
else:
    print ('Grupo B')