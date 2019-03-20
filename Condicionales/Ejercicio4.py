edad=int(input('Tu edad:'))
ingresos=int(input('Tus ingresos:'))
if edad >= 16 and ingresos >= 1000:
    print('Puedes tributar')
else:
    print('No puedes tributar')