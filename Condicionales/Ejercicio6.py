
Ingresos= float(input('¿Cuáles son tus rentas anuales?:'))
if Ingresos < 1000:
    Impositivo = 5
elif Ingresos < 20000:
    Impositivo = 15
elif Ingresos < 35000:
    Impositivo = 20
elif Ingresos < 60000:
    Impositivo = 30
else:
    Impositivo = 45
print('Tipo de impositivo ' + str (Impositivo) + '%')